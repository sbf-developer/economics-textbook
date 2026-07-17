PDF=output/pdf/economics_choices_institutions_power_prosperity.pdf

.PHONY: pdf clean code-test

pdf:
	mkdir -p output/pdf tmp/pdfs
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs book.tex
	makeindex -q -o tmp/pdfs/book.ind tmp/pdfs/book.idx
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs book.tex
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs book.tex
	makeindex -q -o tmp/pdfs/book.ind tmp/pdfs/book.idx
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs book.tex
	cp tmp/pdfs/book.pdf $(PDF)

code-test:
	mkdir -p tmp/mpl
	MPLCONFIGDIR=tmp/mpl python3 code/supply_demand.py --no-plot
	MPLCONFIGDIR=tmp/mpl python3 code/causal_inference_demo.py
	MPLCONFIGDIR=tmp/mpl python3 code/solow_transition.py

clean:
	rm -rf tmp/pdfs output/pdf/*.pdf output/figures
