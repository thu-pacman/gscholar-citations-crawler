# Makefile for the google-scholar-citations

all:

report: citation clean

citation: citation.bib
	- xelatex $@
	- bibtex $@
	- xelatex $@

clean:
	rm -f *.aux *.log *.out *.bbl *.blg *.bcf

clobber: clean
	rm -f *.pdf citation.bib
	rm -rf pdf/
