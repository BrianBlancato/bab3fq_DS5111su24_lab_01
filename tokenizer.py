import string
import logging
import os
from collections import Counter


def clean_text(text):
    '''
    Takes a string and returns all lowercase words without punctuation.

    Args:
        text: An input string to be cleaned.
    
    Returns:
        cleaned_text: The cleaned string with all characters in lowercase and without punctuation.
    '''
    assert isinstance(text, str), 'Input must be a string'

    log.info('Starting text cleaning')
    trans = str.maketrans('', '', string.punctuation)
    cleaned_text = text.lower().translate(trans)

    assert cleaned_text is not None, 'Cleaned text should not be none'
    assert isinstance(cleaned_text, str), 'Cleaned text should be a string'

    log.info('Text is cleaned')
    return cleaned_text


def tokenize(text):
    '''
    Takes a string and reutrns a python list where each item is a word in the file.
    
    Args:
        text: An input string to be tokenized.
    
    Returns:
        tokens: A list of words extracted from the input string.
    '''
    assert isinstance(text, str), 'Input must be a string'

    log.info('Starting tokenization')
    tokens = text.split()

    assert isinstance(tokens, list), 'Tokens should be a list'
    
    log.info('Text has been tokenized')
    return tokens


def count_words(text):
    '''
    Takes a string and returns a dictionary with the words as keys and their counts as value.
    
    Args:
        text: A string for which word frequency is to be counted.

    
    Returns:
        counts: A dictionary with words as keys and their frequency as values.
    '''
    assert isinstance(text, str), 'Input must be a string'

    log.info('Starting word count')
    counts = Counter(text.split())

    assert isinstance(counts, Counter), 'Word count should be a dictionary'

    log.info('Word count is complete')
    return counts


if __name__ == '__main__':

    file_name = os.path.splittext(os.path.basename(__file__))[0]
    logging_file = f"{file_name}"
    logging.basicConfig(level=logging.INFO, filename=logging_file,
                        format='%(asctime)s %(name)s %(levelname)s: %(message)s')
    
log = logging.getLogger(__name__)