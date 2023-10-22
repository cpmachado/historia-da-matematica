SRC = af/af1/af1.tex
DOCS = af1.pdf

af1.pdf: af/af1/af1.tex
	latexmk $(PV) -use-make -pdf $< --auxdir=aux

clean:
	rm -rf aux ${DOCS}

.PHONY: clean watch
