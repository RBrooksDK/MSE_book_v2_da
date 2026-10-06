# Mathematics for Software Engineering: revision register

This file tracks the full technical and editorial review of the book. An item is
only marked complete after the source has been corrected, the book builds, and
the affected PDF pages have been checked.

## Status labels

- `TODO`: confirmed issue, not yet corrected
- `FIXED`: corrected in the LaTeX source, awaiting or having passed build review
- `REVIEW`: wording or convention that needs an explicit editorial decision

## Chapter 0: Basic Arithmetic

- FIXED: Remove duplicated explanation of terms and factors.
- FIXED: Correct a dropped factor in the factorisation examples.
- FIXED: State the real-domain restrictions for radicals.
- FIXED: State the non-zero restrictions for negative integer exponents.
- FIXED: Correct three erroneous rational-exponent calculations.
- FIXED: Explain when applying a function to both sides preserves equivalence.

## Confirmed issues awaiting correction

- FIXED: Chapter 1: logarithm domains, terminology, numerical typo, and stale
  example reference.
- FIXED: Chapter 2: wording and leading-zero contradiction in a conversion example.
- FIXED: Chapter 3: state the universal set explicitly in the counterexample
  involving complements. No other substantive mathematical error was confirmed
  in the first source review.
- FIXED: Chapter 4: restrict the classical probability formula to finite,
  equally likely outcomes; distinguish impossible events from probability-zero
  events.
- FIXED: Chapter 5: correct independence conditions and the interpretation of the
  medical-test example.
- FIXED: Chapter 6: correct variance and standard deviation calculations; revise
  percentile, boxplot, outlier, skewness, and normality claims.
- FIXED: Chapter 7: no substantive mathematical error confirmed in the first
  source review.
- FIXED: Chapter 8: correct the row/column interpretation of matrix-vector
  multiplication and a numerical typo.
- FIXED: Chapter 9: correct identity-matrix dimensions and scope the explicit
  determinant and inverse formulas.
- FIXED: Chapter 10: correct derivative examples and claims about critical points.
- FIXED: Chapter 11: qualify gradient claims and optimisation conclusions.
- FIXED: Chapter 12: correct the number-set diagram, LCM examples, division
  algorithm, factor terminology, and congruence notation.
- FIXED: Chapter 13: correct the definition of logical equivalence and stale
  chapter references.
- FIXED: Chapter 14: separate asymptotic bounds from best/worst-case analysis and
  correct the piecewise-growth example.
- FIXED: Chapter 15: separate case analysis from asymptotic-bound notation,
  correct binary-search and string-matching classifications, state the
  unit-cost model, and correct the operation counts in the sum-of-pairs example.
- FIXED: Synchronise the Important Concepts appendix with the corrected
  probability, statistics, calculus, linear-algebra, logarithm, radical, and
  asymptotic definitions.
- FIXED: Restore and correct the summation appendix, including its telescoping,
  reindexing, powers-of-two, logarithm, and Stirling formulas.
- FIXED: Prevent theorem boxes without explicit labels from generating repeated
  `NoValue` labels; all appendix references now resolve.
- FIXED: Complete a clean multi-pass build of `main_review.pdf` (304 pages) and
  visually inspect representative pages from every revised part. The remaining
  sub-point box-width messages are cosmetic artefacts of the pseudocode package
  and showed no visible clipping in the rendered pages.
