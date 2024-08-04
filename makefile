default:
	@cat makefile

get_texts:
	[ -f pg17192.txt ] || wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt
	[ -f pg932.txt ] || wget https://www.gutenberg.org/cache/epub/932/pg932.txt
	[ -f pg1064.txt ] || wget https://www.gutenberg.org/cache/epub/1064/pg1064.txt
	[ -f pg1063.txt ] || wget https://www.gutenberg.org/cache/epub/1063/pg1063.txt
	[ -f pg51060.txt ] || wget https://www.gutenberg.org/cache/epub/51060/pg51060.txt
	[ -f pg32037.txt ] || wget https://www.gutenberg.org/cache/epub/32037/pg32037.txt
	[ -f pg2148.txt ] || wget https://www.gutenberg.org/cache/epub/2148/pg2148.txt
	[ -f pg2147.txt ] || wget https://www.gutenberg.org/cache/epub/2147/pg2147.txt
	[ -f pg10031.txt ] || wget https://www.gutenberg.org/cache/epub/10031/pg10031.txt
	[ -f pg14082.txt ] || wget https://www.gutenberg.org/cache/epub/14082/pg14082.txt

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
	python3 -m venv env; .env/bin/activate; pip install --upgrade pip; pip install -r requirements.txt

.PHONY: test_non_integration
# Job to run NON integration tests
test_non_integration: lint
	pytest -m "not integration" tests -vv --continue-on-collection-errors > non_integration_test.log 2>&1
#% your tests are passing, however, there is no output when running them. 
# This is ok, just caught me off guard and had to look closer.  In some cases,
# like running in the workflow you might want to enable some output, so the
# logs remain to document that things ran as expected without doubt.

.PHONY: test_integration
# Job to run only integration tests
test_integration: lint
	pytest -m integration tests -vv --continue-on-collection-errors > integration_test.log 2>&1

.PHONY: lint
lint:
	pylint src/bab3fq_package/tokenizer.py || true

