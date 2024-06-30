import pytest
from tokenizer import clean_text
import string
@pytest.mark.parametrize("text, expected_result", [
    ('But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.',
    'but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour')
])

def test_clean_text(text, expected_result):
    cleaned_text = clean_text(text)
    assert cleaned_text == expected_result,  f"Expected: {expected_result}, but got: {clean_text}"

@pytest.mark.parametrize("filename", ["pg17192.txt"])
def test_clean_text_raven(filename):
    with open(filename, 'r') as file:
        content = file.read()
    result = clean_text(content)
    assert isinstance(result, str)
    assert result.islower()
    assert not any(char in string.punctuation for char in result)

 
@pytest.mark.parametrize("filename", [
    "pg17192.txt",
    "pg932.txt",
    "pg1063.txt",
    "pg10031.txt",
    "pg14082.txt"
])

def test_clean_text_english_files(filename):
    with open(filename, 'r') as file:
        text = file.read()
    cleaned_text = clean_text(text)
    assert isinstance(cleaned_text, str)
    assert cleaned_text.islower()
    assert not any(char in string.punctuation for char in cleaned_text)



@pytest.mark.parametrize("text", ["""_Mais le Corbeau, perché solitairement sur ce buste placide, parla 
                         ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je
                         neproférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
                         que je fis à peine davantage que marmotter «D'autres amis déjà ontpris
                         leur vol--demain il me laissera comme mes Espérances déjà ontpris 
                         leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""])

def test_clean_text_french(text):
    result = clean_text(text)
    assert isinstance(result, str)
    assert result.islower()
    assert not any(char in string.punctuation for char in result)


@pytest.mark.parametrize("filename", ["pg14082.txt"])
def test_clean_text_french_raven(filename):
    with open(filename, 'r') as file:
        content = file.read()
    result = clean_text(content)
    assert isinstance(result, str)
    assert result.islower()
    assert not any(char in string.punctuation for char in result)



@pytest.mark.parametrize("filename", [
    "pg17192.txt",
    "pg932.txt",
    "pg1063.txt",
    "pg10031.txt",
    "pg14082.txt",
    "pg14082.txt"
])

def test_clean_text_all_files(filename):
    with open(filename, 'r') as file:
        text = file.read()
    cleaned_text = clean_text(text)
    assert isinstance(cleaned_text, str)
    assert cleaned_text.islower()
    assert not any(char in string.punctuation for char in cleaned_text)


@pytest.mark.skip(reason="Future test for Italian version")

def test_clean_text_italian():
    text = """Ma il Corvo, seduto solitario sul placido busto, pronunciò solo Quella parola, come se la sua anima in quell'unica parola avesse riversato."""
    result = clean_text(text)
    assert isinstance(result, str)
    assert result.islower()
    assert not any(char in string.punctuation for char in result)


@pytest.mark.xfail
def test_clean_text_fail():
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    expected_result = 'but the raven, sitting lonely on the placid bust, spoke only that one word, as if his soul in that one word he did outpour.'
    result = clean_text(text)
    assert result == expected_result
