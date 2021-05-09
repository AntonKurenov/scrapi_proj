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

# print:
# 	@echo $(LOGIN)
# 	@echo $(MONTH)

# print2:
# 	@echo $(LOGIN)
# 	@echo $(MONTH)
# 	@echo $(FLAG)

# ex00:

ex01:
	python3 ./ex01/who_am_i.py $(LOGIN)

start: init token 

token:
	python3 ./connector.py
	cp $(TOKEN) ex00/
	cp $(TOKEN) ex01/
	cp $(TOKEN) ex02/

# cp $(TOKEN) ex01/
# cp $(TOKEN) ex01/
# cp $(TOKEN) ex01/

init:
	pip install -r requirements.txt
	@echo "All dependencies have been installed"
