# MSE_book_v2_da – Matematik for softwareingeniører (dansk)

Dansk udgave af *Mathematics for Software Engineering*. Den engelske kilde i `C:\GitHub\MSE_book_v2` er autoritet for indholdet og må ikke ændres som led i oversættelsesarbejde. Oversat fra commit `6dc0964` (3. september 2026); samme opbygning med fem dele, kapitel 0–15 og to bilag.

## Styrende dokumenter

- `planning/OVERSAETTELSESPRINCIPPER.md` – principper og konventioner.
- `planning/DA_ORDLISTE.md` – bindende dansk terminologi.
- `planning/KILDEFEJL.md` – mulige fejl i den engelske kilde.
- `planning/KONTROLRAPPORT.md` – kontrolrapport for den færdige udgave.
- `planning/AGENT_INSTRUKS.md` – instruks til oversættelse af ét kapitel (bevar al matematik, tal, labels, refs og kode byte for byte; oversæt al læservendt tekst inkl. TikZ/pgfplots-etiketter).

## Værktøjer og kontrol

- `python tools/compare_tex.py <kapitel> | all` – strukturel sammenligning med den engelske kilde (miljøer, labels, refs, formler, tal, kode). Skal give `OK`.
- `python tools/find_english.py` – finder linjer, der stadig ligner engelsk.
- `.\tools\build_chapter.ps1 chapter05 [...]` – bygger kun de valgte kapitler som `work_<kapitel>.pdf`. Undefined refs til andre kapitler er forventelige. Kan tage op til 5 minutter.
- `python tools/render_pages.py <pdf> <mappe> <sider>` – renderer sider til PNG til visuel kontrol.
- `work_*`-filer er git-ignoreret.

## Danske tilpasninger i main.tex

- ElegantBook har ingen `lang=da`. Danske betegnelser (Kapitel, Del, Eksempel, Sætning, Bilag osv.) er sat manuelt i `main.tex`.
- Forsiden laves ved at lægge dansk tekst over det originale forsidebillede (`figure/cover_da.tex`). Danske figurer ligger i `figure/da/`; `tools/make_contour_da.py` laver konturfiguren med danske etiketter.

## Publicering

`main.pdf` er tracket og linkes fra MSE1_26's sessionssider. Et push af `main.pdf` publicerer bogen for de studerende.
