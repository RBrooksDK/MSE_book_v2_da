# Mathematics for Software Engineering

## Description

This repository contains the LaTeX source code for the course book "Mathematics for Software Engineering". The book covers essential mathematical concepts relevant to software engineers, providing foundational knowledge for various areas within computer science. Topics include arithmetic, number theory, numeral systems, Boolean algebra, combinatorics, probability, and linear algebra, among others.

## Target Audience

This book is primarily aimed at undergraduate software engineering students. It may also be beneficial for professional developers looking to refresh or strengthen their understanding of the mathematical principles underlying software development.

## Structure Overview

The book is organized into several chapters covering fundamental mathematical topics relevant to software engineering, along with appendices for supplementary material. *(The specific chapter structure and titles are subject to change.)*

## Building the Book

This book is written in LaTeX using the `elegantbook` class and various other packages (like `tikz`, `circuitikz`, `amsmath`, `pgfplots`, `listings`, `clrscode4e`, `biblatex`).

To compile the book into a PDF:

1.  Ensure you have a working LaTeX distribution installed (e.g., TeX Live, MiKTeX, MacTeX).
2.  Make sure all necessary packages listed in `main.tex` are installed.
3.  Navigate to the root directory of this repository in your terminal.
4.  Run the following command (using `latexmk` is recommended as it handles dependencies and multiple passes):
    ```bash
    latexmk -pdf main.tex
    ```
5.  This will generate `main.pdf`.

## Contributors

*   [Richard Brooks](https://github.com/RBrooksDK)
*   [Eduard Fekete](https://github.com/fredoslav2004)

## License

This project is licensed under the MIT License.
