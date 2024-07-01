import pytest
from tokenizer import tokenize
import subprocess

@pytest.mark.parametrize("text, expected_result", [
    ('But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.',
     ['But', 'the', 'Raven,', 'sitting', 'lonely', 'on', 'the', 'placid', 'bust,', 'spoke', 'only', 'That', 'one', 'word,', 'as', 'if', 'his', 'soul', 'in', 'that', 'one', 'word', 'he', 'did', 'outpour.'])
])
def test_tokenize(text, expected_result):
    tokens = tokenize(text)
    assert tokens == expected_result, f"Expected: {expected_result}, but got: {tokens}"


@pytest.mark.parametrize("Raven", ["pg17192.txt"])
def test_tokenize_raven(Raven):
    with open(Raven, 'r') as file:
        text = file.read()
    result = tokenize(text)
    bash_output = subprocess.check_output(f"cat {Raven} | wc -w", shell=True)
    word_count = int(bash_output)
    assert all(isinstance(word, str) for word in result)
    assert len(result) == word_count


@pytest.mark.parametrize("filename", [
    "pg932.txt",
    "pg1063.txt",
    "pg10031.txt",
    "pg14082.txt"
])
def test_tokenize_english_files(filename):
    with open(filename, 'r') as file:
        text = file.read()
    tokens = tokenize(text)
    bash_output = subprocess.check_output(f"cat {filename} | wc -w", shell=True)
    word_count = int(bash_output.strip())
    assert isinstance(tokens, list) and all(isinstance(t, str) for t in tokens), f"File tokenization failed for {filename}"
    assert len(tokens) == word_count, f"Word count mismatch for {filename}: expected {word_count}, got {len(tokens)}"


@pytest.mark.parametrize("text", ["""_Mais le Corbeau, perché solitairement sur ce buste placide, parla 
                         ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je
                         neproférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
                         que je fis à peine davantage que marmotter «D'autres amis déjà ontpris
                         leur vol--demain il me laissera comme mes Espérances déjà ontpris 
                         leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""])
def test_tokenize_french(text):
    tokens = tokenize(text)
    assert all(isinstance(word, str) for word in tokens)


@pytest.mark.parametrize("french_raven", ["pg14082.txt"])
def test_tokenize_french_raven(french_raven):
    with open(french_raven, 'r') as file:
        text = file.read()
    result = tokenize(text)
    bash_output = subprocess.check_output(f"cat {french_raven} | wc -w", shell=True)
    word_count = int(bash_output)
    assert all(isinstance(word, str) for word in result)
    assert len(result) == word_count


@pytest.mark.parametrize("filename", [
    "pg17192.txt",
    "pg932.txt",
    "pg1063.txt",
    "pg10031.txt",
    "pg14082.txt"
])
def test_tokenize_all_files(filename):
    with open(filename, 'r') as file:
        text = file.read()
    tokens = tokenize(text)
    bash_output = subprocess.check_output(f"cat {filename} | wc -w", shell=True)
    word_count = int(bash_output.strip())
    assert isinstance(tokens, list) and all(isinstance(t, str) for t in tokens), f"File tokenization failed for {filename}"
    assert len(tokens) == word_count, f"Word count mismatch for {filename}: expected {word_count}, got {len(tokens)}"


@pytest.mark.skip(reason="Future test for Italian version")
def test_tokenize_italian():
    text = """Ma il Corvo, seduto solitario sul placido busto, pronunciò solo Quella parola, come se la sua anima in quell'unica parola avesse riversato."""
    tokens = tokenize(text)
    assert all(isinstance(word, str) for word in tokens)

@pytest.mark.xfail
def test_tokenize_fail():
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    expected_result = ['This', 'test', 'should', 'fail.']
    result = tokenize(text)
    assert result == expected_result
