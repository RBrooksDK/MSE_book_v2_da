# Kontrolrapport – dansk udgave af *Mathematics for Software Engineering*

Kilde: `C:\GitHub\MSE_book_v2` (uændret). Dansk udgave: `C:\GitHub\MSE_book_v2_da`, PDF: `main.pdf`.

## Konklusion

- **Hele bogen er oversat:** alle 5 dele, kapitel 0–15, bilag A (Vigtige begreber) og bilag B (Summer), titel, forside, indholdsfortegnelse, LaTeX-etiketter (Figur, Tabel, Eksempel, Sætning, Bilag osv.) og figurer med indlejret engelsk tekst.
- **Alle eksempler er bevaret:** 237 `example`-miljøer i kilden og 237 i den danske udgave, i samme kapitler og rækkefølge. Uformelle eksempler i brødteksten er oversat på deres plads.
- **PDF'en bygger uden indholdsfejl:** 303 sider (som kilden), 0 LaTeX-fejl, 0 udefinerede referencer eller citationer, 0 manglende filer, 0 manglende tegn. 44 overfulde linjer (kilden: 40); de er små og kosmetiske.

## Optælling før og efter

| | Kilde | Dansk |
| --- | --- | --- |
| Dele | 5 | 5 |
| Kapitel-niveau i indholdsfortegnelsen (16 kapitler + bilag + litteratur) | 19 | 19 |
| Afsnit (section) | 64 | 64 |
| Bilag | 2 | 2 |
| `example`-miljøer | 237 | 237 |
| Sider | 303 | 303 |

Strukturtjek (`tools/compare_tex.py all`): miljøer, afsnit, fodnoter, labels, referencer, citationer, punkter, captions, formler, tal og kodeblokke er ens i alle filer. De eneste forskelle er de bevidste afvigelser nedenfor.

Søgning efter engelsk (`tools/find_english.py`): kun tre fund. Det er en pgfplots-kommando, tabeloverskriften »Input« (dansk låneord, som teksten også bruger) og »If-then-else-sætninger« (programmeringsbegreb).

## Bevidste afvigelser

1. **Typografi:** decimalpunktum er bevaret (som i kilden og STA-bogens danske udgave). Tusindtalsseparatoren `10,000` er skrevet `10\,000`. Værdierne er uændrede.
2. **Kode og pseudokode** er byte-identisk med kilden; kun captions er oversat.
3. **Nytegnede figurer med dansk tekst** og samme faglige indhold:
   - kapitel 1: de fire paneler med funktionstyper (`figure/da/function_panels.tex`);
   - kapitel 6: boksplot;
   - kapitel 11: definitions-/værdimængde, konturplot (genereret med forfatterens notebookkode, kun farveskalaens etiket er oversat), topografisk kort (dansk etiket lagt over billedet);
   - kapitel 13: oversigt over logiske gates, transistorbilledet (danske etiketter lagt over);
   - bilag A: Venn-diagrammet over talmængder;
   - forsiden (dansk titel og emneetiketter lagt over omslagsbilledet).
4. **Rettelser af kilden** (alle i `planning/KILDEFEJL.md` under »Rettet«):
   - kapitel 1: forkert hårdkodet eksempelnummer erstattet af `\autoref`;
   - kapitel 2: \(0.6875_{10} = 0.1011_2\) (binært punktum manglede);
   - kapitel 4: danske ordenstal »1., 2. eller 3. præmie«;
   - kapitel 5: »In this section« i kapitelindledningen oversat »I dette kapitel«;
   - kapitel 9: verbet »span« flyttet ud af formlen;
   - kapitel 12: stavefejlen »GFC« rettet til GCF;
   - kapitel 15: en afbrudt sætning (linje 1402) fuldført ud fra de efterfølgende captions;
   - bilag B: `\unskip` efter `\For` fjerner et fejlplaceret mellemrum (kun layout).

Øvrige mulige fejl i kilden (over 50 punkter) er registreret med fil og linje i `planning/KILDEFEJL.md` og oversat uændret.

## Punkter til menneskelig gennemgang

- **Faglige fejl i kilden, som ikke er rettet:**
  - kapitel 10, linje 399–400: en afledt mangler;
  - kapitel 15: forkerte totaler i Java-kommentarerne på linje 1393 og 1698 og et forkert iterationsantal i Loop1 (linje 1050–1052);
  - kapitel 5: terningmængden;
  - bilag A, linje 1289: nummereringen af kædereglen.
- **Terminologi:**
  - »fakultet« for *factorial*;
  - forkortelserne GCD/LCM;
  - »Indgang/Udgang« i transistorfiguren, mens brødteksten bruger »input/output«;
  - »FOIL-loven« beholdt med dansk forklaring;
  - »halerekursion« og »memoisering«.
- **Boksplottet** følger etiketterne i det originale billede, også dem, der er registreret som upræcise.
- **Litteraturlisten:** feltet »Accessed online« og »John Wiley; Sons« kommer fra bibliografifilen og er ikke ændret.
- **Datoen** på titelsiden er sat til »Maj 2025« efter kilden.
