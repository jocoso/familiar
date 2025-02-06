install:
	pip3 install -r requirements.txt

populate:
	pip3 list --format=freeze > requirements.txt

test:
	py.test tests

exec:
	python3 sample/sample.py
	
.PHONY: install populate test exec
