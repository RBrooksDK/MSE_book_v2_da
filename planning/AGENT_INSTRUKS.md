# Instruks til oversættelse af et kapitel

Du oversætter en del af lærebogen *Mathematics for Software Engineering* (MSE1)
af Richard Brooks (VIA University College) fra engelsk til dansk. Bogen er
forfatterens egen, MIT-licenserede LaTeX-kilde, og forfatteren har bestilt
den danske udgave.

- Engelsk kilde (må IKKE ændres): `C:\GitHub\MSE_book_v2\<fil>.tex`
- Dansk projekt: `C:\GitHub\MSE_book_v2_da\` – her ligger en kopi af den
  engelske fil, som du skal erstatte med den danske oversættelse.

## Læs først (obligatorisk)

1. `C:\GitHub\MSE_book_v2_da\planning\OVERSAETTELSESPRINCIPPER.md`
2. `C:\GitHub\MSE_book_v2_da\planning\DA_ORDLISTE.md` (bindende terminologi)
3. Referencekapitlerne – sammenlign engelsk og dansk for at ramme tone og
   håndtering af eksempler, løsninger og formler:
   `C:\GitHub\MSE_book_v2\chapter05.tex` ↔ `C:\GitHub\MSE_book_v2_da\chapter05.tex`
   (og evt. chapter00).

## Opgave

Oversæt hele filen, fra første til sidste linje. Skriv den danske fil i sin
helhed (UTF-8). Store filer må gerne skrives i flere omgange, men intet må
mangle. Alt læservendt engelsk skal oversættes: overskrifter, brødtekst,
eksempeltitler, opgaver, løsninger, mellemregningernes tekst, `\text{...}` i
formler, billedtekster, tabelindhold, tekst i TikZ/pgfplots-diagrammer
(akseetiketter, `legend entries`, noder), fodnoter, punktlister.

Bevar uændret: al matematik, alle tal, labels, refs, cites, miljøer,
layoutkommandoer, rækkefølge, programkode og pseudokode (byte-for-byte, også
kommentarer i koden), identifikatorer, filnavne, datasætnavne og egennavne.
Opfind ikke nye eksempler, udelad ingen, og tilføj ingen forklaringsafsnit.

## Kontrol (skal være udført, før du afslutter)

Kør i PowerShell fra `C:\GitHub\MSE_book_v2_da`:

1. `python tools\compare_tex.py <fil>` – skal give `OK`. Hvis der er
   forskelle, så ret oversættelsen, indtil kun tilsigtede forskelle er tilbage
   (fx serielt komma, der forsvinder i en inline-formel), og forklar dem.
2. `.\tools\build_chapter.ps1 <fil>` – skal give `errors=0`
   (»undefined-refs« til andre kapitler er forventelige i et kapitelbuild).
   Bygget kan tage op til 5 minutter; brug lang timeout.
3. `python tools\render_pages.py work_<fil>.pdf C:\GitHub\tmp\mse_da <sider>`
   og se på mindst 4 sider med tætte formler, tabeller og figurer. Ret
   layoutfejl, som oversættelsen har skabt (fx tekst, der stikker ud af en
   figur eller tabel).
4. Læs din oversættelse igennem afsnit for afsnit mod kilden: er alle
   sætninger, forbehold, eksempler og løsninger med? Er der engelske rester?
   Søg fx efter ` the `, ` and `, ` of `, ` is `, `Example`, `where`.

Du må ikke ændre andre filer end dem, du er tildelt, bortset fra midlertidige
`work_*`-filer. Du må ikke køre git-kommandoer. Rør ikke `main.tex`,
værktøjerne eller planlægningsfilerne.

## Svar tilbage (kort, struktureret)

1. Fil(er) oversat, og resultat af `compare_tex.py` og build (sider, errors).
2. Mulige faglige fejl i den engelske kilde med præcis `fil:linje` og
   beskrivelse (ret dem IKKE, medmindre fejlen er entydig og rettelsen
   nødvendig – beskriv i så fald præcis, hvad du ændrede).
3. Nye fagtermer, du har valgt, som ikke stod i ordlisten (engelsk → dansk).
4. Eventuelle bevidste afvigelser fra kilden og punkter, der kræver menneskelig
   gennemgang.
