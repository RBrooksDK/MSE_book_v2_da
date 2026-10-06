# Matematik for softwareingeniører

Dette repository indeholder LaTeX-kilden til den **danske udgave** af
lærebogen *Mathematics for Software Engineering* (MSE1) af Richard Brooks,
VIA University College.

Den engelske udgave ligger i et separat projekt (`MSE_book_v2`) og er
autoritet for indholdet. Den danske udgave er oversat fra commit
`6dc0964e5e5ad896e1ef2d09234ab64f33c2e315` (3. september 2026) og har samme
opbygning: fem dele, kapitel 0–15 og to bilag.

## Build

```powershell
latexmk -pdf main.tex
```

ElegantBook har ingen indbygget `lang=da`; danske betegnelser (Kapitel, Del,
Eksempel, Sætning, Bilag osv.) er sat i `main.tex`. Forsiden genskabes på
dansk ved at lægge tekst over det originale forsidebillede
(`figure/cover_da.tex`).

Under arbejdet med et enkelt kapitel kan man bygge det alene:

```powershell
.\tools\build_chapter.ps1 chapter05
```

## Kvalitetskontrol

- `python tools/compare_tex.py all` sammenligner hver dansk fil med den
  engelske kilde: miljøer, labels, henvisninger, citater, alle formler, tal i
  teksten og programkode.
- `python tools/find_english.py` finder linjer, der stadig ligner engelsk.
- `python tools/render_pages.py main.pdf <mappe> <sider>` renderer sider til
  visuel kontrol.

## Redaktionelle dokumenter

- `planning/DA_ORDLISTE.md` – bindende dansk terminologi
- `planning/OVERSAETTELSESPRINCIPPER.md` – principper og konventioner
- `planning/KILDEFEJL.md` – mulige fejl fundet i den engelske kilde
- `planning/KONTROLRAPPORT.md` – kontrolrapport for den færdige udgave

## Forfattere

* [Richard Brooks](https://github.com/RBrooksDK)
* [Eduard Fekete](https://github.com/fredoslav2004)

## Licens

Projektet er udgivet under MIT-licensen.
