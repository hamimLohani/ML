# Machine Learning Theory Notes — LaTeX Template

This template is crafted for creating high-quality, beautifully typeset theory and revision notes for Machine Learning and Statistics, based on the layout and visual system used across the **Ridge Regression** and **Lasso Regression** notes.

---

## 📁 Directory Structure

```text
your_topic_notes/
├── template.tex          # (Rename to main.tex or your_topic.tex)
├── figures/              # Place your diagram PNG/PDF files here
├── README.md             # Documentation & compilation instructions
└── template.pdf          # Compiled reference preview
```

---

## 🚀 Quick Start & Compilation

Compile with `pdflatex` (run twice to generate the Table of Contents, page numbers, and cross-references):

```bash
pdflatex template.tex
pdflatex template.tex
```

Or using `latexmk`:

```bash
latexmk -pdf template.tex
```

---

## 🎨 Visual System & Color Palette

The template uses a carefully curated academic color palette:

| Color Name | Hex Code | Purpose / Usage |
| :--- | :--- | :--- |
| **Navy** | `#17324D` | Chapter titles, section headings, primary emphasis |
| **Blue** | `#2878B5` | Subsection headings, `keyidea` callout frames |
| **Teal** | `#168477` | Subsubsection headings, `intuition` callout frames |
| **Gold** | `#D18B26` | `warningbox` callout frames, critical alerts |
| **PaleBlue** | `#EDF5FB` | Background for `keyidea` boxes |
| **PaleTeal** | `#EAF6F3` | Background for `intuition` boxes |
| **PaleGold** | `#FFF6E6` | Background for `warningbox` callouts |
| **Ink** | `#263238` | Primary body text |
| **Muted** | `#61717D` | Header, footer, and metadata text |
| **CodeBg** | `#F7F8FA` | Source code listing background |

---

## 📦 Styled Callout Environments

### 1. Key Idea (`keyidea`)
Used for core definitions, foundational laws, and key takeaways:
```latex
\begin{keyidea}[title=Core concept]
Lasso balances fit and simplicity by augmenting RSS with an L1 penalty.
\end{keyidea}
```

### 2. Intuition (`intuition`)
Used for geometric visualizations, analogies, and conceptual models:
```latex
\begin{intuition}[title=Geometric diamond]
The L1 constraint has corners on axes, causing level curves to hit sparse vertices first.
\end{intuition}
```

### 3. Important Note / Warning (`warningbox`)
Used for edge cases, common pitfalls, and regularity conditions:
```latex
\begin{warningbox}[title=Feature scaling]
Always standardize features before fitting regularized linear models!
\end{warningbox}
```

### 4. Worked Example (`worked`)
Used for algebraic derivations, step-by-step arithmetic, or proof steps:
```latex
\begin{worked}[title=Soft thresholding calculation]
Given z = 3.5 and threshold = 1.0, S(3.5, 1.0) = 2.5.
\end{worked}
```

---

## 💻 Code Snippets (`listings`)

The template includes syntax highlighting configured for Python:

```latex
\begin{lstlisting}
import numpy as np

def soft_threshold(z, threshold):
    return np.sign(z) * max(abs(z) - threshold, 0.0)
\end{lstlisting}
```

---

## 📐 Document Architecture

1. **Title Page**: Minimalist, elegant book-style title with author and institution.
2. **Front Matter**: Automatic Roman numbering for Table of Contents.
3. **Main Matter**: Arabic numbering starting on Chapter 1:
   - **Chapter 1: The Big Picture & Motivation** (Intuition, high-level overview, comparison table).
   - **Chapter 2: Mathematical Foundations & Derivations** (Loss formulation, step-by-step proofs).
   - **Chapter 3: Algorithm & Implementation** (Numerical optimization, Python code).
   - **Chapter 4: Practical Considerations & Tuning** (Standardization, cross-validation).
   - **Chapter 5: Revision Sheet & Self-Test** (Essential formula reference sheet, conceptual checklist, self-test questions, and short answer key).
