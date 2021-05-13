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
CAMPUS = campus

TOKEN = token.out
.PHONY: token init start ex00 ex01 ex02 ex03

ex00:

start: init ex00 ex01 ex02 ex03

token:
	python3 ./connector.py
	cp $(TOKEN) ex00/
	cp $(TOKEN) ex01/
	cp $(TOKEN) ex02/
	cp $(TOKEN) ex03/
	cp $(TOKEN) experiments/

ex01:
	@echo "ex01"
	python3 ./ex01/who_am_i.py $(LOGIN)

ex02:
	@echo "ex02"
	python3 ./ex02/me_myself.py $(LOGIN)
	
ex03:
	@echo "ex03"
	python3 ./ex03/campus.py $(CAMPUS) $(MONTH) $(YEAR)

# cp $(TOKEN) ex01/
# cp $(TOKEN) ex01/
# cp $(TOKEN) ex01/

init:
	pip install -r requirements.txt
	@echo "All dependencies have been installed"
