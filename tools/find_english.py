"""List lines in the Danish sources that still look like English prose.

Usage: python tools/find_english.py [file ...]   (default: all book files)

Math, code listings, pseudocode, comments, label/ref arguments and file names
are removed first; a line is reported when it contains several common English
function words. Each hit needs a human decision: some are legitimate (titles
of cited works, code identifiers, proper names, or an English term given in
parentheses).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = [f"chapter{i:02d}.tex" for i in range(16)] + ["concepts.tex", "appendix01.tex",
                                                      "main.tex", "figure/number_sets_venn.tex"]
# Words that are also Danish (for, to, by, let, given, ...) are deliberately excluded.
WORDS = r"the|and|of|is|are|with|that|this|we|which|from|can|it|its|not|or|where|when|then|if|each|our|these|those|has|have|was|will|let's|between|into|than|such|example|solution|you|your|there|what|how|any|all|only|also|must|should|would|could"
WORD_RE = re.compile(r"(?<![\w\\])(" + WORDS + r")(?![\w])", re.I)


def clean(text):
    text = re.sub(r"\\begin\{(lstlisting|codebox|verbatim)\}.*?\\end\{\1\}",
                  lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    lines = []
    for line in text.split("\n"):
        line = re.sub(r"(?<!\\)%.*", "", line)
        line = re.sub(r"\\(?:label|ref|autoref|eqref|cite|input|includegraphics|usepackage|"
                      r"inlinecode|texttt|lstinline|url|href|begin|end|Procname|proc|id|const|"
                      r"usetikzlibrary|definecolor|colorlet|newcommand|renewcommand)\*?"
                      r"(\[[^\]]*\])?\{[^}]*\}", " ", line)
        line = re.sub(r"\\\(.*?\\\)|\$[^$]*\$", " ", line)
        lines.append(line)
    return lines


def main(paths):
    total = 0
    for rel in paths:
        path = ROOT / rel
        if not path.exists():
            continue
        in_display = False
        for n, line in enumerate(clean(path.read_text(encoding="utf-8")), 1):
            if re.search(r"\\\[|\\begin\{(equation|align|gather)", line):
                in_display = True
            hits = WORD_RE.findall(line)
            if not in_display and len(hits) >= 2:
                total += 1
                print(f"{rel}:{n}: {line.strip()[:170]}")
            if re.search(r"\\\]|\\end\{(equation|align|gather)", line):
                in_display = False
    print(f"-- {total} suspicious lines")


if __name__ == "__main__":
    main(sys.argv[1:] or FILES)
