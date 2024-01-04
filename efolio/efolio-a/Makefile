SRC = 2200909efolioA.tex
DOCS = 2200909efolioA.pdf
DATA = $(wildcard data/*.csv)


2200909efolioA.pdf: 2200909efolioA.tex
	latexmk -auxdir=aux -pdflatex $(PV) -use-make -pdf $<


data/ex1.csv: codigo/ex1.py
	@python codigo/ex1.py 5 > data/ex1.csv

data/ex2.csv: codigo/ex2.py
	@python codigo/ex2.py > data/ex2.csv

clean:
	@latexmk -C -bibtex ${SRC}
	@rm -rf aux ${DOCS}

.PHONY: clean ${DOCS}
