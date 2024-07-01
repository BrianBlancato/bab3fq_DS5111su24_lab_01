import pytest
from collections import Counter
from tokenizer import count_words
import subprocess

@pytest.mark.parametrize("text, expected_result", [
    ('But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.',
     {'But': 1, 'the': 2, 'Raven,': 1, 'sitting': 1, 'lonely': 1, 'on': 1, 'placid': 1, 'bust,': 1, 'spoke': 1, 'only': 1, 'That': 1, 'one': 2, 'word,': 1, 'as': 1, 'if': 1, 'his': 1, 'soul': 1, 'in': 1, 'that': 1, 'word': 1, 'he': 1, 'did': 1, 'outpour.': 1})
])
def test_count_words(text, expected_result):
    word_counts = count_words(text)
    assert word_counts == expected_result, f"Expected: {expected_result}, but got: {word_counts}"

@pytest.mark.parametrize("Raven", ["pg17192.txt"])
def test_count_words_raven(Raven):
    with open(Raven, 'r') as file:
        text = file.read()
    
    word_counts = count_words(text)
    total_words = sum(word_counts.values())
    bash_output = subprocess.check_output(f"cat {Raven} | wc -w", shell=True)
    bash_word_count = int(bash_output.strip())
    assert total_words == bash_word_count, f"Word count mismatch for {Raven}: expected {bash_word_count}, got {total_words}"


@pytest.mark.parametrize("filename", [
    "pg17192.txt",
    "pg932.txt",
    "pg1063.txt",
    "pg10031.txt"
])
def test_count_words_english_files(filename):
    with open(filename, 'r') as file:
        text = file.read()
    word_counts = count_words(text)
    total_words = sum(word_counts.values())
    bash_output = subprocess.check_output(f"cat {filename} | wc -w", shell=True)
    bash_word_count = int(bash_output.strip())
    assert total_words == bash_word_count, f"Word count mismatch for {filename}: expected {bash_word_count}, got {total_words}"


@pytest.mark.parametrize("text", ["""_Mais le Corbeau, perché solitairement sur ce buste placide, parla 
                         ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je
                         neproférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
                         que je fis à peine davantage que marmotter «D'autres amis déjà ontpris
                         leur vol--demain il me laissera comme mes Espérances déjà ontpris 
                         leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""])
def test_count_words_french(text):
    bash_output = subprocess.check_output(f"echo \"{text}\" | wc -w", shell=True)
    bash_word_count = int(bash_output)

    word_counts = count_words(text)
    total_words = sum(word_counts.values())
    assert total_words == bash_word_count, f"Expected {bash_word_count} words, got {total_words}"


@pytest.mark.parametrize("french_raven", ["pg14082.txt"])
def test_count_words_french_raven(french_raven):
    with open(french_raven, 'r') as file:
        text = file.read()
    
    word_counts = count_words(text)
    total_words = sum(word_counts.values())
    bash_output = subprocess.check_output(f"cat {french_raven} | wc -w", shell=True)
    bash_word_count = int(bash_output.strip())
    assert total_words == bash_word_count, f"Word count mismatch for {french_raven}: expected {bash_word_count}, got {total_words}"


@pytest.mark.parametrize("filename", [
    "pg17192.txt",
    "pg932.txt",
    "pg1063.txt",
    "pg10031.txt",
    "pg14082.txt"
])
def test_count_words_all_files(filename):
    with open(filename, 'r') as file:
        text = file.read()
    word_counts = count_words(text)
    total_words = sum(word_counts.values())
    bash_output = subprocess.check_output(f"cat {filename} | wc -w", shell=True)
    bash_word_count = int(bash_output.strip())
    assert total_words == bash_word_count, f"Word count mismatch for {filename}: expected {bash_word_count}, got {total_words}"


@pytest.mark.skip(reason="Future test for Italian version")
def test_count_words_italian():
    text = """Ma il Corvo, seduto solitario sul placido busto, pronunciò solo Quella parola, come se la sua anima in quell'unica parola avesse riversato."""
    bash_output = subprocess.check_output(f"echo \"{text}\" | wc -w", shell=True)
    bash_word_count = int(bash_output)

    word_counts = count_words(text)
    total_words = sum(word_counts.values())
    assert total_words == bash_word_count, f"Expected {bash_word_count} words, got {total_words}"

@pytest.mark.xfail
def test_count_words_fail():
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    expected_result = {'This':1, 'test':1, 'should':1, 'fail.':1}
    result = count_words(text)
    assert result == expected_result