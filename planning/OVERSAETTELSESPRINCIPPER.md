# Oversættelsesprincipper for den danske udgave af MSE1

Kilde: `C:\GitHub\MSE_book_v2`, commit `6dc0964e5e5ad896e1ef2d09234ab64f33c2e315`
(3. september 2026). Kilden er autoritet for indholdet. Kapitel 0 og 5 er
referencekapitler for tone og håndtering af eksempler.

## Grundregel

Oversæt tro mod originalen. Bevar indhold, niveau, struktur, progression,
eksempler, talværdier, enheder, antagelser og konklusioner. Tilføj ikke nye
forklaringer, eksempler eller afsnit, og udelad intet.

## LaTeX-struktur

- Bevar alle miljøer, `\label`, `\ref`, `\autoref`, `\cite`, `\input`,
  `\includegraphics`, figurer, tabeller, fodnoter, `\newpage`, mellemrum og
  layoutkommandoer præcis som i kilden. Rækkefølgen af elementer bevares.
- Label-navne oversættes **ikke** (fx `\label{ex:renal-disease}` bevares).
- LaTeX-kommentarer (`% ...`) må gerne bevares på engelsk; de er ikke
  læservendte.
- Eksempeltitler, der står efter `\begin{example}` i brødteksten
  (fx `\begin{example} Factorisation`), oversættes på samme plads.
- Overskrifter i `\chapter`, `\section`, `\subsection`, `\caption`,
  `\begin{definition}[...]`, `\begin{theorem}{...}` osv. oversættes.
- Danske bogstaver skrives direkte i UTF-8 (æ, ø, å).

## Matematik

- Formler, symboler og variabelnavne bevares uændret. Bogstavsymboler, der
  stammer fra engelske ord (fx `G` for girl, `H` for heads), ændres ikke;
  forklar dem kort i teksten, hvis koblingen ellers forsvinder
  (»\(G\) betegner en pige (af engelsk »girl«)«).
- Tekst inde i matematik (`\text{...}`, `\textnormal{...}`, `\mathrm{...}`
  med ord) oversættes, når den er læservendt: `\text{and}` → `\text{og}`,
  `\text{where}` → `\text{hvor}`, `\text{Healthy}` → `\text{Rask}`.
  Funktionsnavne og forkortelser (`\mathrm{d}`, `\operatorname{Var}`,
  `\text{mod}`, `\gcd`, `\text{lcm}`) bevares.
- Decimaltal skrives med **decimalpunktum** som i kilden (0.05, 3.14). Det er
  en bevidst konvention (som i den danske STA-bog), fordi bogen blander
  matematik og programkode, og fordi komma bruges som separator i koordinater,
  intervaller og mængder.
- Tusindtalsseparator: engelsk `10,000` eller `10{,}000` skrives `10\,000`
  (tyndt mellemrum), både i tekst og formler. Værdien er uændret. Tal uden
  separator i kilden (fx 1000) bevares uden separator.
- Procent skrives som i kilden (`5\%`).

## Kode og identifikatorer

- `lstlisting`, `codebox`, `verbatim`, `\inlinecode{...}`, `\texttt{...}`
  med kode, CLRS-pseudokode (`\begin{codebox}`, `\Procname`, `\li` osv.),
  variabelnavne, funktionsnavne, filnavne og datasætnavne bevares
  **byte-for-byte**. Kommentarer inde i kode bevares også, så koden forbliver
  identisk med kilden.
- Billedtekster til algoritmer (`caption=...` i lstlisting) oversættes.

## Litteratur, navne

- Titler på citerede værker, forfatternavne, egennavne og firmanavne bevares.
- Kendte personnavne i genitiv: Bayes' sætning, Ohms lov, De Morgans love,
  Pascals trekant, Eulers tal.

## Sprog

- Skriv korrekt, naturligt og let forståeligt dansk. Del lange engelske
  sætninger op, når det giver bedre dansk; bevar alle nuancer, forbehold og
  logiske forbindelser.
- Brug »vi« og »du« som i kilden (engelsk »we« → »vi«, »you« → »du«).
- Brug danske anførselstegn »...«.
- Brug kommaregler med startkomma kun, hvor det er nødvendigt; sæt komma
  før ledsætninger (»at«, »som«, »hvis«, »når«).
- Brug tankestreg ` -- ` for engelsk ` - ` / `—` som tankestreg.
- Undgå engelsk ordstilling, »indeholdende«, »hvorved« osv. Vælg mundret
  fagdansk.
- Engelske fagudtryk bruges kun, hvor de er gængse i dansk undervisning
  (fx bit, byte, hardware, software, firewall, gate). Hvis et engelsk fagord
  ikke har en etableret dansk pendant, kan det angives én gang i parentes:
  »irrationel rod (på engelsk \emph{surd})«.
- Faste betegnelser: se `DA_ORDLISTE.md`.

## Mulige fejl i kilden

- Ret ikke stiltiende. Registrér mulige fejl i `KILDEFEJL.md` med fil og
  linjenummer i den engelske kilde.
- Ret kun, når fejlen er entydig og rettelsen nødvendig; beskriv rettelsen
  i `KILDEFEJL.md` under »Rettet«. Ved tvivl: oversæt som kilden og registrér.
- Rent sproglige småfejl i kilden (stavefejl, dobbeltord) oversættes blot
  korrekt uden registrering.

## Kontrol pr. kapitel

1. `python tools/compare_tex.py chapterNN` skal give `OK` (eller kun
   forklarede, tilsigtede forskelle).
2. `.\tools\build_chapter.ps1 chapterNN` skal give `errors=0`.
3. Gennemse renderede sider (`python tools/render_pages.py ...`) med tætte
   formler, tabeller og figurer.
4. Sammenlign afsnit for afsnit med kilden.
