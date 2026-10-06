# Register over mulige fejl i den engelske kilde

Linjenumre henviser til den engelske kilde i `C:\GitHub\MSE_book_v2`
(commit `6dc0964`). Medmindre andet står under »Rettet«, er punktet oversat
som i kilden og kræver menneskelig vurdering.

## Registreret, ikke rettet

| Fil:linje | Beskrivelse |
| --- | --- |
| chapter00.tex:217 | Advarslen »Never do« viser \(\frac{a}{b}+\frac{c}{d}=\frac{a+b}{b+d}\). Den typiske fejl, man advarer mod, er sandsynligvis \(\frac{a+c}{b+d}\) (tæller \(a+b\) ser ud som en tastefejl). Advarslen er stadig sand og er bevaret uændret. |
| chapter05.tex:24 | \(B\) beskrives som »udfaldet er større end eller lig med 3«, men angives som \(\{3,4,5\}\); for en sekssidet terning er det \(\{3,4,5,6\}\), hvilket ville give \(P(A\mid B)=1/2\) i stedet for \(2/3\). Bevaret som i kilden. |
| chapter05.tex:359–370 | Halvlederscenariet definerer \(A\) = forurenet chip og \(B\) = svigt og spørger efter sandsynligheden for svigt, men udledningen opdeler \(A\) og giver \(P(A)=P(A\cap B)+P(A\cap B^c)\); spørgsmålet besvares ikke talmæssigt. Rollerne for \(A\) og \(B\) virker byttet om. Bevaret. |
| chapter05.tex:449–451 | Teksten taler først om at opdele »en hændelse B« og siger derefter, at »hændelsen A er opdelt i fem … hændelser \(B_1,\dots,B_5\), som tilsammen udgør udfaldsrummet«; det er udfaldsrummet, der er opdelt. Bevaret. |

## Rettet

| Fil:linje | Rettelse |
| --- | --- |
| chapter05.tex:4 | »In this section« i kapitelindledningen er oversat »I dette kapitel«, da teksten indleder et kapitel. Ren redaktionel præcisering. |
