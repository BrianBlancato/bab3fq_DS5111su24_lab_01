import pytest
from collections import Counter
from tokenizer import count_words

@pytest.mark.parametrize("text, expected_result", [
    ('But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.',
     {'But': 1, 'the': 2, 'Raven,': 1, 'sitting': 1, 'lonely': 1, 'on': 1, 'placid': 1, 'bust,': 1, 'spoke': 1, 'only': 1, 'That': 1, 'one': 2, 'word,': 1, 'as': 1, 'if': 1, 'his': 1, 'soul': 1, 'in': 1, 'that': 1, 'word': 1, 'he': 1, 'did': 1, 'outpour.': 1})
])

def test_count_words(text, expected_result):
    word_counts = count_words(text)
    assert word_counts == expected_result, f"Expected: {expected_result}, but got: {word_counts}"

@pytest.mark.parametrize("filename", [
    "pg932.txt",
    "pg1063.txt",
    "pg10031.txt",
    "pg14082.txt"
])

def test_count_words_english_files(filename):
    with open(filename, 'r') as file:
        text = file.read()
    word_counts = count_words(text)
    assert isinstance(word_counts, Counter), f"File word count failed for {filename}"
