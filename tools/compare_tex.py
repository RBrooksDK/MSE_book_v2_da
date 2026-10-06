"""Structural comparison of an English source file and its Danish translation.

Usage: python tools/compare_tex.py chapter00 [chapter05 ...]   (or: all)

For each file the script compares, between source and translation:
  * environment counts (\\begin{...}), sectioning commands, footnotes
  * labels, references and citations (as multisets)
  * every math segment ($...$, \\(...\\), \\[...\\], equation/align/... bodies),
    after removing \\text{...}-style words, which are expected to be translated
  * numbers occurring in running text
  * graphics, inputs and code listings (listings must be byte-identical)
Any difference is printed. "OK" means no structural difference was found.
"""
import collections
import pathlib
import re
import sys

SRC = pathlib.Path(r"C:\GitHub\MSE_book_v2")
DST = pathlib.Path(__file__).resolve().parent.parent

FILES = [f"chapter{i:02d}" for i in range(16)] + ["concepts", "appendix01"]

MATH_ENVS = r"equation\*?|align\*?|aligned|gather\*?|multline\*?|eqnarray\*?|alignat\*?|flalign\*?"
TEXT_CMDS = r"\\(?:text|textnormal|textrm|textbf|textit|mbox|textsl|mathrm|operatorname|intertext|textsf|texttt|emph)\s*\{"


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def remove_text_args(m):
    """Replace the argument of text-like commands inside math by a placeholder."""
    out, i = [], 0
    for mt in re.finditer(TEXT_CMDS, m):
        if mt.start() < i:
            continue
        out.append(m[i:mt.start()])
        depth, j = 1, mt.end()
        while j < len(m) and depth:
            depth += {"{": 1, "}": -1}.get(m[j], 0)
            j += 1
        arg = m[mt.end():j - 1]
        # keep any nested math and digits so numbers are still compared
        keep = "".join(re.findall(r"\$[^$]*\$|\\\(.*?\\\)|\d+(?:\.\d+)?", arg))
        out.append("\\T{" + keep + "}")
        i = j
    out.append(m[i:])
    return "".join(out)


def normalise_math(m):
    m = remove_text_args(m)
    m = re.sub(r"\s+", "", m)
    # sentence punctuation at the end of a formula follows the host language
    m = re.sub(r"(?:[,.;:]|\\,|\\;|\\quad)+$", "", m)
    return m


def math_segments(s):
    segs = []
    for env in re.finditer(r"\\begin\{(" + MATH_ENVS + r")\}(.*?)\\end\{\1\}", s, re.S):
        segs.append(env.group(2))
    s2 = re.sub(r"\\begin\{(" + MATH_ENVS + r")\}(.*?)\\end\{\1\}", " ", s, flags=re.S)
    segs += re.findall(r"\\\[(.*?)\\\]", s2, re.S)
    s2 = re.sub(r"\\\[(.*?)\\\]", " ", s2, flags=re.S)
    segs += re.findall(r"\\\((.*?)\\\)", s2, re.S)
    s2 = re.sub(r"\\\((.*?)\\\)", " ", s2, flags=re.S)
    segs += re.findall(r"\$\$(.*?)\$\$", s2, re.S)
    s2 = re.sub(r"\$\$(.*?)\$\$", " ", s2, flags=re.S)
    segs += re.findall(r"(?<!\\)\$(.+?)(?<!\\)\$", s2, re.S)
    s2 = re.sub(r"(?<!\\)\$(.+?)(?<!\\)\$", " ", s2, flags=re.S)
    return [normalise_math(x) for x in segs], s2


def listings(s):
    # the optional [...] argument (caption=...) is reader-facing and translated
    return re.findall(r"\\begin\{(lstlisting|codebox|verbatim)\}(?:\[[^\]]*\])?(.*?)\\end\{\1\}", s, re.S)


def text_numbers(rest):
    rest = re.sub(r"\\begin\{(lstlisting|codebox|verbatim)\}.*?\\end\{\1\}", " ", rest, flags=re.S)
    rest = re.sub(r"\\(?:label|ref|autoref|eqref|cite|input|includegraphics|pageref|hyperref)(\[[^\]]*\])?\{[^}]*\}", " ", rest)
    rest = re.sub(r"\\(?:begin|end)\{[^}]*\}(\[[^\]]*\])?(\{[^}]*\})?", " ", rest)
    rest = re.sub(r"\[[^\]]*(?:width|scale|height|angle|trim|xshift|yshift)[^\]]*\]", " ", rest)
    rest = re.sub(r"\\(?:hspace|vspace|setlength|addtolength|renewcommand|arraystretch|setcounter|rule)\*?\{[^}]*\}(\{[^}]*\})?", " ", rest)
    return re.findall(r"(?<![A-Za-z\\])\d+(?:[.,]\d+)?", rest)


def features(path):
    s = strip_comments(path.read_text(encoding="utf-8"))
    # English thousands separators (10,000 or 10{,}000) are written 10\,000 in
    # the Danish edition; the value is the same, so compare digit groups only.
    s = re.sub(r"(?<=\d)(?:,|\{,\}|\\,|\\ |~)(?=\d{3}(?!\d))", "", s)
    f = {}
    f["env"] = collections.Counter(re.findall(r"\\begin\{([^}]+)\}", s))
    f["section"] = collections.Counter(re.findall(r"\\((?:sub)*section|chapter|part|paragraph)\*?[\[{]", s))
    f["footnote"] = collections.Counter(["fn"] * len(re.findall(r"\\footnote\b", s)))
    f["label"] = collections.Counter(re.findall(r"\\label\{([^}]*)\}", s))
    f["ref"] = collections.Counter(re.findall(r"\\(?:auto|eq|page|c|C)?ref\{([^}]*)\}", s))
    f["cite"] = collections.Counter(re.findall(r"\\(?:text|paren|foot)?cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", s))
    f["graphics"] = collections.Counter(re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", s))
    f["input"] = collections.Counter(re.findall(r"\\input\{([^}]*)\}", s))
    f["item"] = collections.Counter(["item"] * len(re.findall(r"\\item\b", s)))
    f["caption"] = collections.Counter(["caption"] * len(re.findall(r"\\caption\b", s)))
    segs, rest = math_segments(s)
    f["math"] = collections.Counter(segs)
    f["textnum"] = collections.Counter(text_numbers(rest))
    f["listing"] = collections.Counter(x[1] for x in listings(s))
    return f


def compare(name):
    a = features(SRC / f"{name}.tex")
    b = features(DST / f"{name}.tex")
    problems = []
    for key in a:
        if a[key] != b[key]:
            only_a = a[key] - b[key]
            only_b = b[key] - a[key]
            problems.append((key, only_a, only_b))
    print(f"== {name}: " + ("OK" if not problems else f"{len(problems)} categories differ"))
    print(f"   examples src={a['env']['example']} da={b['env']['example']}, "
          f"math segments src={sum(a['math'].values())} da={sum(b['math'].values())}")
    for key, oa, ob in problems:
        print(f"   [{key}]")
        for k, v in oa.items():
            print(f"      only in source x{v}: {k[:160]!r}")
        for k, v in ob.items():
            print(f"      only in Danish x{v}: {k[:160]!r}")
    return not problems


if __name__ == "__main__":
    names = FILES if sys.argv[1:] == ["all"] else sys.argv[1:]
    ok = all([compare(n) for n in names])
    sys.exit(0 if ok else 1)
