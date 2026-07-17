# ECONOMICS: Choices, Institutions, Power, and Prosperity

Editable source and teaching materials for the compact textbook by Scott Brodie Forsyth.

## Build

Requirements: a LaTeX installation with `pdflatex`, `makeindex`, and the packages listed in `book.tex`.

```bash
make pdf
```

The build runs LaTeX, creates the index, and places the final PDF in `output/pdf/economics_choices_institutions_power_prosperity.pdf`.

## Contents

- `book.tex` - complete manuscript and typesetting source.
- `code/` - tested Python demonstrations used in the text.
- `data/` - a small transparent teaching dataset and notes on official sources.
- `references.md` - source-audit notes and links to official data and primary research.
- `output/pdf/` - rendered book.

The numerical CSV supplied here is explicitly simulated for teaching. It is not presented as official country data. The source-audit notes identify official datasets suitable for replacing it in classroom work.

## Reproducibility

The scripts use Python's standard library plus NumPy and Matplotlib. They write figures to `output/figures/` and print key calculations. Run:

```bash
python3 code/supply_demand.py
python3 code/causal_inference_demo.py
python3 code/solow_transition.py
```

All code was executed during final review in the supplied environment.

## Scope and edition

This is a compact, evidence-led edition. It teaches the core models and methods, states assumptions, and points to primary sources without pretending that a short volume can replace specialist graduate texts. Empirical claims are geographically and historically scoped where possible. Current official statistics should be refreshed from the linked source before reuse in a new edition.
