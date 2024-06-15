default:
	@cat makefile

get_texts:
	wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt
	wget https://www.gutenberg.org/cache/epub/932/pg932.txt
	wget https://www.gutenberg.org/cache/epub/1064/pg1064.txt
	wget https://www.gutenberg.org/cache/epub/1063/pg1063.txt
	wget https://www.gutenberg.org/cache/epub/51060/pg51060.txt
	wget https://www.gutenberg.org/cache/epub/32037/pg32037.txt
	wget https://www.gutenberg.org/cache/epub/2148/pg2148.txt
	wget https://www.gutenberg.org/cache/epub/2147/pg2147.txt
	wget https://www.gutenberg.org/cache/epub/2149/pg2149.txt
	wget https://www.gutenberg.org/cache/epub/2150/pg2150.txt

raven_line_count:
	cat pg17192.txt | wc -l

raven_word_count:
	cat pg17192.txt | wc -w

raven_counts:
	cat pg17192.txt | grep  raven | wc -l
	cat pg17192.txt | grep Raven | wc -l
	cat pg17192.txt | grep -E "(raven|Raven)" | wc -l

total_lines:
	wc -l *.txt

total_words:
	wc -w *.txt

setup:
	python3 -m venv env
	pip install --upgrade pip
	pip install -r requirements.txt

