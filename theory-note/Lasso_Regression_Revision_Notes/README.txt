LASSO REGRESSION — REVISION NOTES

Contents
- main.tex: complete LaTeX source.
- Lasso_Regression_Revision_Notes.pdf: compiled preview.
- figures/: five PNG diagrams used by the document.

Compile
1. Keep main.tex and the figures/ directory together.
2. Compile main.tex with pdfLaTeX.
3. For a local TeX Live installation, run:

   pdflatex main.tex
   pdflatex main.tex

The second run updates the table of contents and cross-references.

Overleaf
1. Create a Blank Project.
2. Upload main.tex and the complete figures/ folder (or upload the ZIP and extract its contents in the project).
3. Set the compiler to pdfLaTeX.
4. Recompile.

Notes
- The mathematical derivations consistently use RSS + lambda * ||beta||_1.
- Therefore, the soft-threshold in the coordinate update is lambda/2.
- If a textbook uses (1/2)RSS + lambda * ||beta||_1, the threshold is lambda instead.
- The regularization-path plot is an illustrative diagram, not measured data.
