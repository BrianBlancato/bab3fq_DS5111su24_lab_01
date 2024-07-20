import pytest
from tokenizer import clean_text
import string


# Test clean_text against given statemnet
@pytest.mark.parametrize("text, expected_result", [
    ('But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.',
    'but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour')
])
def test_clean_text(text, expected_result):
    # Given the text statement and expected result
    # When the text statement is passed through the clean_text function
    # Then the returned text should only contain lowercase, no punctuation and be equal to the expected result.
    cleaned_text = clean_text(text)
    assert cleaned_text == expected_result,  f"Expected: {expected_result}, but got: {clean_text}"


# Test clean_text against the Raven file
@pytest.mark.parametrize("filename", ["pg17192.txt"])
def test_clean_text_raven(filename):
    # Given the Raven text file
    # When the text file is passed through the clean_text function
    # Then the returned object should be a string of lowercase letters and no punctuation.
    with open(filename, 'r') as file:
        content = file.read()
    result = clean_text(content)
    assert isinstance(result, str)
    assert result.islower()
    assert not any(char in string.punctuation for char in result)

 
 # Test clean_text against all English files
@pytest.mark.parametrize("filename", [
    "pg17192.txt",
    "pg932.txt",
    "pg1063.txt",
    "pg10031.txt"
])
def test_clean_text_english_files(filename):
    # Given all English text files
    # When each text file is individually passed through the clean_text function
    # Then each returned object should be a string of lowercase letters and no punctuation.
    with open(filename, 'r') as file:
        text = file.read()
    cleaned_text = clean_text(text)
    assert isinstance(cleaned_text, str)
    assert cleaned_text.islower()
    assert not any(char in string.punctuation for char in cleaned_text)


# Test clean_text against given French statement
@pytest.mark.parametrize("text", ["""_Mais le Corbeau, perché solitairement sur ce buste placide, parla 
                         ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je
                         neproférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
                         que je fis à peine davantage que marmotter «D'autres amis déjà ontpris
                         leur vol--demain il me laissera comme mes Espérances déjà ontpris 
                         leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""])
def test_clean_text_french(text):
    # Given a French text statement
    # When the French text statement is passed through clean_text function
    # Then the returned object should be a string of lowercase characters and no punctuation.
    result = clean_text(text)
    assert isinstance(result, str)
    assert result.islower()
    assert not any(char in string.punctuation for char in result)


# Test clean_text against the French Raven file
@pytest.mark.parametrize("filename", ["pg14082.txt"])
def test_clean_text_french_raven(filename):
    # Given the French Raven File
    # When the French Raven text file is passed through the clean_text function
    # Then the returned object should be a string of lowercase characters and no punctuation.
    with open(filename, 'r') as file:
        content = file.read()
    result = clean_text(content)
    assert isinstance(result, str)
    assert result.islower()
    assert not any(char in string.punctuation for char in result)


# Test clean_text against all text files
@pytest.mark.parametrize("filename", [
    "pg17192.txt",
    "pg932.txt",
    "pg1063.txt",
    "pg10031.txt",
    "pg14082.txt"
])
def test_clean_text_all_files(filename):
    # Given all text files
    # When all text files are passed through the clean_text function
    # Then each returned object should be a string of lowercase letters and no punctuation.
    with open(filename, 'r') as file:
        text = file.read()
    cleaned_text = clean_text(text)
    assert isinstance(cleaned_text, str)
    assert cleaned_text.islower()
    assert not any(char in string.punctuation for char in cleaned_text)


# Test skipping an Italian string for clean_text
@pytest.mark.skip(reason="Future test for Italian version")
def test_clean_text_italian():
    # Given an Italian text string
    # When the Italian text is passed through the clean_text function
    # Then the returned object should be a string of lowercase letters and not punctuation.
    text = """Ma il Corvo, seduto solitario sul placido busto, pronunciò solo Quella parola, come se la sua anima in quell'unica parola avesse riversato."""
    result = clean_text(text)
    assert isinstance(result, str)
    assert result.islower()
    assert not any(char in string.punctuation for char in result)


# Test clean_text against a statement that is intended to fail on purpose.
@pytest.mark.xfail
def test_clean_text_fail():
    # Given a string and an incorrect expected result
    # When the text string is passed through clean_text
    # Then the test should fail because the result will not match the purposely incorrect expected result.
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    expected_result = 'but the raven, sitting lonely on the placid bust, spoke only that one word, as if his soul in that one word he did outpour.'
    result = clean_text(text)
    assert result == expected_result
