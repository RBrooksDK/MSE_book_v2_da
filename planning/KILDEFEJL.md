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

| chapter14.tex:133 | »\(n^2 < 2^n\) for any integer \(n \geq 4\)« gælder ikke for \(n=4\) (\(16=16\)); skal være \(n\geq 5\) eller \(\leq\). To mulige rettelser, derfor bevaret. |
| chapter14.tex:965 | \(\lim_{n\to\infty} f(n)/g(n) = 2\sin(n)+3\) er ikke en gyldig grænseværdi (afhænger af \(n\)); teksten forklarer bagefter, at grænseværdien ikke eksisterer. Bevaret. |
| chapter14.tex:636, 750 | »grows slower/faster … but not necessarily at the same rate« er uklart; lille o/ω udelukker netop samme vækstrate. Oversat ordret. |
| chapter14.tex:9, 168, 282 | Mindre: \(O\) i stedet for \(\mathcal{O}\) (l. 9); figuren plotter \(\ln x\), men teksten taler om \(\log_2\) (l. 168); »for all three notations«, selv om eksemplet kun behandler store \(\mathcal{O}\) (l. 282). Bevaret. |
| chapter14.tex:60 | Redigeringsrest: »In Section \ref{sec:ch10sec1}the introduction to this chapter«. Oversat som »I afsnit …, kapitlets indledning, …«. |

| chapter10.tex:399–400 | Sætningen »The derivative is« slutter uden udregning; \(f'(x)=\frac{1}{2\sqrt{x}}\) og \(f'(4)=\frac14\) mangler. Oversat ufuldstændigt som i kilden – bør udfyldes af forfatteren. |
| chapter10.tex:1078, 1142–1158 | For \(f(x)=2(x^3-12x^2+45x)-99\) er \(f(2)=1=f(5)\) (efterregnet); det globale minimum på \([2,7]\) antages også i endepunktet \(x=2\), men tekst og billedtekst nævner kun \(x=5\). Bevaret. |
| chapter10.tex:370–375 | Eksemplet med \((x^2+1)^3\) bruger kædereglen i afsnittet om potensreglen, før kædereglen er indført. Bevaret. |
| chapter10.tex:715 | `\text { (where } u=…` – parentesen lukkes ikke. Bevaret. |
| chapter10.tex:1253 | Definitionen af den anden afledte siger »provided the limit exists«, men formlen indeholder ingen grænseværdi. Bevaret. |
| chapter10.tex:1067, 865 | »critical point« bruges uden definition (ellers »stationary point«); »stationary point of inflection or simply inflection point« blander stationært vendepunkt og vendepunkt generelt. Bevaret. |
| chapter10.tex:126 | Grænseværdien 5 viser Θ(\(n^2\)), hvilket er stærkere end det angivne \(\mathcal{O}(n^2)\). Upræcist, ikke forkert. Bevaret. |

| chapter01.tex:276 | `\begin{example}{label:}` sætter den bogstavelige tekst »label:« i eksemplet. Bevaret. |
| chapter01.tex:553 | \(10^{0.477\ldots}\) mod 0.4771… andre steder. Lille inkonsekvens; bevaret. |
| chapter02.tex:61 | »the first place after the decimal being the \(2^0\) position« – \(2^0\)-pladsen står foran punktummet. Oversat ordret. |
| chapter02.tex:481, 525, 569, 615 | »Add the Rightmost Column … column 1 (from counting from MSB)« er selvmodsigende; der tælles fra LSB. Oversat som kilden. |
| chapter02.tex:70 | Tabellen erklærer 5 kolonner, men bruger 4. Ingen synlig fejl. |

| chapter03.tex:361 | Mængdealgebra og boolesk algebra kaldes »dually isomorphic«; potensmængdealgebraen er isomorf med en boolesk algebra. Oversat »dualt isomorfe«. |
| chapter04.tex:366–368 | Maria-eksemplet (koncertbilletter) har ingen løsning/svar. Mulig udeladelse; bevaret. |
| chapter06.tex:442 | Ufuldstændig sætning (»… examplifies .«); oversat »… giver et eksempel«. |
| chapter06.tex:691 | 95. percentil forklares som »95% er hurtigere«, mens definitionen (l. 688) siger »på eller under«. Bevaret. |
| chapter06.tex:846 | Kurtosis lovet forklaret i næste afsnit, men forklares aldrig. Bevaret. |
| chapter06.tex:853 | Henviser til boksplot og outliers, som først behandles senere (l. 1187, 1236). Bevaret. |
| chapter06.tex:1029–1033 mod 1099 | Skævhed defineres via »mean > median«, men l. 1099 siger, at rækkefølgerne ikke er definitioner. Bevaret. |
| figure/boxplot.png mod chapter06.tex:1249–1256 | Billedet kalder grænserne Q1−1.5·IQR/Q3+1.5·IQR »whisker« og knurhårenes ender »Minimum/Maximum value«, selv om der er outliers udenfor; strider mod tekstens definition. Den danske figur følger billedet (se kontrolrapporten). |
| chapter08.tex:1242, 1270 | `\text{for all } s, t \in \mathbb{R}`, men parametrene er \(x_2, x_3\). Bevaret. |
| chapter08.tex:1404 | Beskrivelsen af »the last part of the theorem« passer på del (b), ikke (c). Bevaret. |
| chapter08.tex:1444–1485 | Kun tre af seks par tjekkes, men konklusionen gælder alle par (konklusionen er korrekt). Bevaret. |
| chapter09.tex:660 | »property (4)«, men punkterne er nummereret (a)–(d); der menes (d). Bevaret. |
| chapter09.tex:199, 1263 | Manglende `&` i en matrix; nulvektor skrevet `\overline{0}`. Bevaret. |
| chapter11.tex:239 | Pilene siges at pege fra lyse (lave) mod mørke (høje) farver; farveskalaen i `contour_with_gradients.png` viser det modsatte. Bevaret. |
| chapter11.tex:359 | »effectively concludes this book«, men bogen fortsætter med kapitel 12–15. Bevaret. |
| figure/topographic-map.png | Stavefejl »Hilly terrian« i billedet. Dansk etiket »Bakket terræn«. |
| chapter12.tex:124 | At hypotenusen er \(\sqrt2\), »viser« ikke, at \(\sqrt2\) er irrational. Bevaret. |
| chapter13.tex:28 | Shannons speciale og »Alfred Noble«-prisen: årstallet (1939/1940) bør verificeres. Bevaret. |
| chapter13.tex:244, 390, 551, 600, 304 | Mindre: ulogisk »since they are not strictly necessary« (oversat »selv om …«); \(\bar x\bar y+x=\bar y+x\) under absorptionslovene; »gates operate within transistors« (omvendt); funktionel fuldstændighed sidestillet med universel gate; eksemplet lukkes før løsningen. Bevaret. |
| chapter15.tex:1392–1393 | Javakommentar `T(n) = 4 + 7 + 14`; korrekt er `4 + 7 + 3 = 14`. Overflødigt kolon i »3 time units:«. Kode bevaret. |
| chapter15.tex:1698 | `2 + (4n+1) + 3 + 1 = 4n + 6`; summen er \(4n+7\). Kode bevaret. |
| chapter15.tex:1050–1052 | Loop1: antal iterationer angivet som \(\lceil\log_3 n\rceil\); korrekt er \(\lfloor\log_3 n\rfloor+1\) (fx én iteration for \(n=1\)). Bevaret. |
| chapter15.tex:1372–1374 | Opsummeringen nummererer linje 1–3, analysen bruger linje 2–4. Bevaret. |
| chapter15.tex:873 | \(\sum_{i=1}^n = i\) skal være \(\sum_{i=1}^n i\). Bevaret. |
| chapter15.tex:149–150 | Teksten nævner arrayet `A`, pseudokoden bruger `arr`. Bevaret. |
| chapter15.tex:603, 650 | `Factorial4` kalder `Factorial`, `Naive-Fibonacci` kalder `Fibonacci` (navne passer ikke). Kode bevaret. |
| chapter15.tex:1276 | Loop6 siges at »udføre« \((\log_2 n)(n+1)-n+2\) operationer; udledningen giver kun en øvre grænse. Bevaret. |
| chapter15.tex:908–910 | Summen kaldes antal iterationer for den indre løkke; den er det samlede antal. Bevaret. |
| concepts.tex:1289 | `\setcounter{enumi}{6}` står før `\begin{enumerate}`, så kædereglen nummereres 1 i stedet for 7. Bevaret. |
| concepts.tex:856 | »the coefficient matrix above«, men der er ingen matrix ovenfor i bilaget. Bevaret. |
| concepts.tex:1200, 1203 | Nulvektor skrevet `\overline{0}`; verbet »span« sat som operator i formlen. Bevaret. |
| concepts.tex:1302–1305 | Potensreglens formel står to gange. Bevaret. |
| concepts.tex:678 | Bayes' sætning: første lighed forudsætter også \(P(B)>0\). Bevaret. |
| concepts.tex:408 | »dually isomorphic« er upræcist (algebraerne er isomorfe). Oversat som i kilden. |
| concepts.tex:1258 | Potensreglen »for any real n« uden forbeholdet om definitionsmængde i linje 1302. Bevaret. |

## Rettet

| Fil:linje | Rettelse |
| --- | --- |
| chapter12.tex (»GFC«) | Entydig stavefejl for GCF; skrevet GCF. |
| chapter09.tex:1266 | Formlen `$A \operatorname{span} \mathbb{R}^n$` indeholdt verbet; skrevet »Søjlerne i \(A\) udspænder \(\mathbb{R}^n\)«. Kun typografisk omskrivning, samme udsagn. |
| chapter04.tex:335 | `$1^{\text{st}}, 2^{\text{nd}}$, or $3^{\text{rd}}$` skrevet som »1., 2. eller 3. præmie« (dansk ordenstal). |
| chapter01.tex:781 | Hårdkodet »From the results of Example 3« pegede på et forkert nummer; det omtalte eksempel (»Find \(\log_5 17\)«, linje 756) er Eksempel 1.13. Eksemplet har fået `\label{ex:log5-17}`, og teksten bruger `\autoref`. |
| chapter02.tex:100 | \(0.6875_{10} = 1011_2\) rettet til \(0.6875_{10} = 0.1011_2\) (det binære punktum manglede; tabellen og 101.1011 ovenfor bekræfter værdien). |
| chapter15.tex:1402 | Ufuldstændig sætning »we present an algorithm to perform the« fuldført som »… en algoritme, der udfører iterativ binær søgning.« Ud fra de efterfølgende listing-captions. |
| appendix01.tex (`\For`) | Makroen `\For` i `clrscode4e.sty` giver et mellemrum før komma (»for ,«); `\unskip` tilføjet. Kun layout. |
| chapter05.tex:4 | »In this section« i kapitelindledningen er oversat »I dette kapitel«, da teksten indleder et kapitel. Ren redaktionel præcisering. |
