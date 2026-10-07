# Kontrolrapport – dansk og engelsk udgave af *Mathematics for Software Engineering*

Kilde: `C:\GitHub\MSE_book_v2` (oprindeligt commit `6dc0964`). Dansk udgave:
`C:\GitHub\MSE_book_v2_da`. Begge udgaver er efterfølgende rettet efter
`planning/KILDEFEJL.md`.

## Status efter fejlrettelserne 7. oktober 2026

- Begge bøger er bygget med `latexmk -pdf main.tex`: engelsk er 302 sider, dansk er 303 sider efter de opfølgende rettelser.
- De færdige logs har 0 LaTeX-fejl og 0 udefinerede referencer eller citationer. Dansk log har ingen linjer, der går mere end 5 pt ud i margen.
- Alle 5 dele, kapitel 0–15, begge bilag og 237 `example`-miljøer er bevaret i begge udgaver.
- Kode og pseudokode er ens i udgaverne efter de samme rettelser, også engelske kodekommentarer i den danske bog.
- Engelsk `figure/topographic-map.png` har nu “Hilly terrain”. Ændringen omfatter kun 526 pixels i etikettens område; resten af billedet er identisk med det tidligere bitmap.
- De 17 resterende punkter i gruppe C i `planning/KILDEFEJL.md` er ikke ændret i bøgerne og kræver forfatterens stillingtagen. Punktet om Shannons pris er efterprøvet og lukket uden bogrettelse.

## Struktursammenligning

`python tools/compare_tex.py all` viser kun disse allerede kendte forskelle fra
den danske oversættelses kontrol. Værktøjets exitkode er 1, fordi det markerer
bevidste grafik- og typografiforskelle som afvigelser. De øvrige 13 af 18 filer
vises som `OK`, herunder alle rettede formler og kodeblokke.

| Fil | Dokumenteret forskel |
| --- | --- |
| `chapter01.tex` | De engelske `figure/book1.png`–`book4.png` er samlet i danske `figure/da/function_panels.tex`; sammenligneren ser derfor kun kildens fire rasterfiler. |
| `chapter04.tex` | Engelske ordenstal `1^{st}`, `2^{nd}`, `3^{rd}` er danske `1.`, `2.`, `3.`. Det giver to manglende matematiksegmenter og tre ekstra tal i dansk løbende tekst, men værdier og betydning er uændrede. |
| `chapter06.tex` | Engelsk `figure/boxplot.png` er tegnet som `figure/da/boxplot_da.tex` i den danske udgave. Tal-forskellen `0.7` er en figurparameter, ikke en ændring i bogens data. |
| `chapter11.tex` | Dansk bruger `figure/da/domainrange_da.tex`, `figure/da/contour_da.png` og en dansk tekstoverlejring på det topografiske kort. Tal-forskellen `0.5` er en figurparameter. |
| `chapter13.tex` | Dansk bruger `figure/da/gates_da.tex` og danske etiketter over `logicincomp.png`. Tal-forskellene `0.8` og `0.9` er figurparametre. |

Sammenligneren finder ingen yderligere forskelle i miljøer, kapitler og afsnit,
eksempler, labels, henvisninger, citationer, formler, kodeblokke eller tal i
undervisningsteksten. Forskelle i bogens bilag og bibliografi er behandlet i
`planning/KILDEFEJL.md`.

## Danske oversættelsesvalg, der fortsat gælder

- Decimalpunktum er bevaret. Tusindtalsseparatoren er et tyndt mellemrum som i `10\,000`.
- Danske figurtekster, LaTeX-etiketter, indholdsfortegnelse og omslag er bevaret.
- Danske figurer med indlejret tekst er tegnet eller overlejret som beskrevet i tabellen ovenfor.
- Egennavne, citationsnøgler og programidentifikatorer er bevaret.
