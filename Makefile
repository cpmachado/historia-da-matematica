DOCS = 2200909efolioA.pdf

2200909efolioA.pdf: efolio/efolio-a/2200909efolioA.pdf
	cp $< $@

efolio/efolio-a/2200909efolioA.pdf:
	make -C efolio/efolio-a 2200909efolioA.pdf

clean:
	@rm -rf aux ${DOCS}

.PHONY: clean ${DOCS}
