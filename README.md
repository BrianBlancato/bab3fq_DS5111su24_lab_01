# Text Processing

This repository provides a set of functions for text processing such as text cleaning, tokenizing text and counting word frequencies.

## Description

The reposirty contains the following main functions in tokenizer:
1. **clean_text**: takes a string and returns all lowercase words and throws out any punctuation
2. **tokenize**: takes a string and returns a python list, where each item is a word in the file
3. **count_words**: takes a string and returns a dictionary with the words as keys, and their counts as value

## Usage

### Example
Below is an example demonstraing how to use the functions:

'''{python}

from tokenizer import clean_text, tokenize, count_words

text = "Hello world, the sky is blue, and the grass is green!"

# Clean the text
cleaned_text = clean_text(text)
print(cleaned_text)
# Output: 'hello world the sky is blue and the grass is green'  
  
# Tokenize the cleaned text
tokens = tokenize(cleaned_text)
print(tokens)
# Output: ['hello', 'world', 'the', 'sky', 'is', 'blue', 'and', 'the', 'grass', 'is', 'green']
  
# Count the words  
word_count = count_words(cleaned_text)
print(word_count)
# Output: Count({'hello':1, 'world':1, 'the':2, 'sky':1, 'is':2, 'blue':1, 'and':1, 'grass':1, 'green':1})
'''