import pytest
from tokenizer import tokenize

@pytest.mark.parametrize("text, expected_result", [
    ('But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.',
     ['But', 'the', 'Raven,', 'sitting', 'lonely', 'on', 'the', 'placid', 'bust,', 'spoke', 'only', 'That', 'one', 'word,', 'as', 'if', 'his', 'soul', 'in', 'that', 'one', 'word', 'he', 'did', 'outpour.'])
])

def test_tokenize(text, expected_result):
    tokens = tokenize(text)
    assert tokens == expected_result, f"Expected: {expected_result}, but got: {tokens}"


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
    assert isinstance(tokens, list) and all(isinstance(t, str) for t in tokens), f"File tokenization failed for {filename}"