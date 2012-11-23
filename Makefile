fontlog:
	python FONTLOG.py > FONTLOG.txt

franklin:
	python franklin.py franklin.ufo franklin.otf

2steps:
	python 2steps.py 2steps.ufo 2steps.otf

roquette:
	python La_roquette.py La_roquette.ufo La_roquette.otf

all:
	python franklin.py franklin.ufo franklin.otf
	python 2steps.py 2steps.ufo 2steps.otf
	python La_roquette.py La_roquette.ufo La_roquette.otf

