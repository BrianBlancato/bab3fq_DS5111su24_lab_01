import pytest
from collections import Counter
from tokenizer import count_words
import subprocess
from tokenizer import tokenize
from tokenizer import clean_text
import string
import os


# Test to download text files
@pytest.mark.integration
def test_get_text():
    # Given a list of files and a directory
    # When the test is run
    # Then the files should be downloaded in the directory
    lab_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = [
        'pg17192.txt',
        'pg932.txt',
        'pg1064.txt',
        'pg1063.txt',
        'pg51060.txt',
        'pg32037.txt',
        'pg2148.txt',
        'pg2147.txt',
        'pg10031.txt',
        'pg14082.txt'
    ]
    for file in files:
        file_path = os.path.join(lab_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    r = subprocess.run(['make', 'get_texts'], cwd=lab_dir, capture_output=True, text=True, check=True)
    assert r.returncode == 0, "Failed to run 'make get_texts'."

    for file in files:
        file_path = os.path.join(lab_dir, file)
        assert os.path.isfile(file_path), f"{file} was not downloaded"


# Test all tests from tokenizer.py
@pytest.mark.integration
@pytest.mark.parametrize("Raven", ["pg17192.txt"])
def test_complex_raven(Raven):
    # Given the Raven text file
    # When the Raven text file is passed through clean_text, tokenize and count_words from tokenizer.py
    # Then checks the return of the functions with expected returns.
    with open(Raven, 'r') as file:
        text = file.read()

    cleaned_text = clean_text(text)
    assert isinstance(cleaned_text, str)
    assert cleaned_text.islower()
    assert not any(char in string.punctuation for char in cleaned_text)

    tokenized_text = tokenize(cleaned_text)
    assert all(isinstance(word, str) for word in tokenized_text)

    word_counts = count_words(cleaned_text)
    word_counts_expected = Counter(tokenized_text)
    assert word_counts == word_counts_expected