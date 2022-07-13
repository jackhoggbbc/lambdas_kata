.PHONY: challenge1 challenge2 clean

venv: requirements.txt
	python3 -m venv venv && source ./venv/bin/actviate && pip install -r $<

challenge1: venv
	source ./venv/bin/activate && nosetests challenge1/test.py

challenge2: venv
	source ./venv/bin/activate && nosetests challenge2/test.py

