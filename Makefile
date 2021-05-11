# All needed for this assignment
# init rule for installing all packages
# pip install oauthlib
# python -m pip install requests
# pip install requests-oauthlib

LOGIN = login
MONTH = month
YEAR = year
FLAG = flag
PROJECT = project

TOKEN = token.out
.PHONY: token init start

ex00:

start: init token ex00 ex01 ex02

ex01:
	python3 ./ex01/who_am_i.py $(LOGIN)

ex02:
	python3 ./ex02/me_myself.py $(LOGIN)

token:
	python3 ./connector.py
	cp $(TOKEN) ex00/
	cp $(TOKEN) ex01/
	cp $(TOKEN) ex02/
	cp $(TOKEN) ex03/

# cp $(TOKEN) ex01/
# cp $(TOKEN) ex01/
# cp $(TOKEN) ex01/

init:
	pip install -r requirements.txt
	@echo "All dependencies have been installed"
