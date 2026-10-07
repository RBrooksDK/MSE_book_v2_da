# Kildefejl i *Mathematics for Software Engineering*

Linjerne nedenfor henviser til den engelske kilde i commit `6dc0964`. Den danske
udgave har tilsvarende steder, men linjerne kan afvige. Rettelserne i begge
udgaver er lavet efter efterregning. Gruppe C er uændret i bøgerne.

## Registreret, ikke rettet — forfatterbeslutninger (gruppe C)

| Kilde | Konkret forslag til forfatteren |
| --- | --- |
| `chapter05.tex:359–370` | Beslut, om eksemplet skal beregne `P(B)=0.20·0.10+0.80·0.005=0.024`; skriv da udregningen og behold A som forurening og B som svigt. |
| `chapter05.tex:449–451` | Lad `B_1,…,B_5` være en partition af udfaldsrummet, og beskriv `A∩B_i` som delene af A. |
| `chapter04.tex:366–368` | Tilføj en kort løsning til Maria-eksemplet, eller markér det som en opgave uden løsning. |
| `chapter13.tex:304` | Flyt `\end{example}` efter løsningen, hvis løsningen skal indgå i eksemplet. |
| `chapter13.tex:600` | Skeln mellem en funktionelt fuldstændig samling operatorer og en enkelt universel gate; NAND og NOR er hver for sig universelle. |
| `chapter15.tex:603,650` | Beslut, om de rekursive kald skal hedde `Factorial4`/`Naive-Fibonacci` som procedurerne, eller om procedureoverskrifterne skal ændres. Ret kode og pseudokode i begge udgaver ens. |
| `chapter10.tex:370–375` | Flyt eksemplet med `(x²+1)³` til efter kædereglen, eller giv en kort henvisning frem til den. |
| `chapter10.tex:865,1067` | Definér “critical point” før sætningen, og skeln mellem stationært vendepunkt og vendepunkt generelt. |
| `chapter10.tex:126` | Beslut, om eksemplet skal konkludere `Θ(n²)` ud fra den positive endelige grænse og nævne O som en følge. |
| `chapter06.tex:853` | Flyt omtalen af boksplot og outliers til efter deres introduktion, eller nøjes her med histogrammer. |
| `chapter06.tex:1029–1033,1099` | Definér skævhed via halens retning og angiv mean–median-rækkefølgen som en typisk, ikke nødvendig, egenskab. |
| `figure/boxplot.png`, `chapter06.tex:1249–1256` | Ret figurens etiketter, så 1.5·IQR-værdierne er hegn, knurhårenes ender er de yderste observationer inden for hegnene, og outliers ligger udenfor. Ret også den danske tegning. |
| `chapter08.tex:1444–1485` | Kontrollér alle seks par, eller begrund hvorfor de tre viste par er tilstrækkelige for konklusionen. |
| `chapter11.tex:239` | Sammenhold pilene med farveskalaen og beskriv høj/lav-værdierne efter figurens faktiske farver. |
| `chapter01.tex:553` | Vælg en ensartet præcision for logaritmen: `0.4771…` eller `0.477…` overalt. |
| `chapter02.tex:70` | Ret tabellens kolonneformat fra fem til fire kolonner, hvis kildens formattering skal være teknisk konsekvent. |
| `reference.bib` | Fjern én af de to “Accessed online”-angivelser for Thomas og skriv Montgomery-forlagets ampersand som `\&` eller `and`. Punktet står i gruppe C, selv om den oprindelige punkttekst også siger “Ret bib-filen”; ingen bibliografiposter er ændret. |

## Efterprøvet, ingen bogrettelse

| Kilde | Kontrol |
| --- | --- |
| `chapter13.tex:28` | [ASCE's officielle vinderliste](https://www.asce.org/career-growth/awards-and-honors/alfred-noble-prize/alfred-noble-prize-past-award-winners) anfører Claude E. Shannon under 1939 og bruger stavningen “Alfred Noble Prize”. Bogens år og prisnavn står derfor korrekt. |

## Opfølgende rettelser efter review 7. oktober 2026

| Aktuelt sted | Rettelse |
| --- | --- |
| `chapter05.tex:193` | `67/137` er rettet til cirka `0.4891` og `48.91%` i begge udgaver. |
| `chapter05.tex:315,356` | Bemærkningen bruger nu den faktiske marginale `P(B)=0.68`; det fejlagtige uafhængighedsprodukt er `0.272`, mens `P(A∩B)=0.32`. |
| `chapter02.tex:63,70` | Gentagen heltalsdivision og rest beskrives korrekt, og tabeloverskriften viser `⌊x_n/2⌋`. |
| `chapter14.tex:576,953` | Ω(1)-udsagnet er afgrænset til positive konstante funktioner; O/Ω-eksemplet henviser til begge propositioner. |
| `chapter11.tex:351` | Gradientnedstigning er kvalificeret med en passende læringsrate i begge udgaver. |
| `chapter15.tex:890` | Dansk præciserer, at det er outputtets talværdi, som vokser kvadratisk. |
| `chapter03.tex:362`, `concepts.tex:408` | Sammenhængen med boolesk algebra er afgrænset til delmængder af en fast universalmængde. |
| `chapter01.tex:642`, `concepts.tex:144` | Produktreglen for logaritmer viser eksplicit `log(xy)` i begge udgaver. |
| `chapter01.tex:89`, `chapter04.tex:3`, `chapter06.tex:66,671–672,699` | Henvisning, gentagelse og mellemrum før `ms` er rettet i begge udgaver. |
| Kun dansk: `chapter03.tex:282`, `chapter04.tex:17,82`, `chapter05.tex:15`, `concepts.tex:30`, `figure/da/overlay_images.tex` | Sprog og sats er justeret; den danske log har nu ingen linjer, der går mere end 5 pt ud i margen. |

## Rettet

| Kilde i commit `6dc0964` | Rettelse |
| --- | --- |
| `chapter10.tex:399–400` | Udledningen `f'(x)=1/(2√x)` og `f'(4)=1/4` er indsat efter kontrol af `f(x)=√x`. |
| `chapter15.tex:1392–1393` | Java-kommentaren er `4+7+3=14`; overflødigt kolon efter “3 time units” er fjernet i begge udgaver. |
| `chapter15.tex:1698` | Konstantleddet i `2+(4n+1)+3+1` er rettet fra 6 til 7 i begge kodeblokke. |
| `chapter15.tex:1050–1052` | Loop1 kører `⌊log₃ n⌋+1` gange for `n≥1`; formel og konklusion er rettet. |
| `chapter15.tex:873` | Summen er rettet til `Σᵢ₌₁ⁿ i`. |
| `chapter15.tex:1372–1374` | Opsummeringen bruger nu linje 2, 3 og 4 som analysen. |
| `chapter15.tex:149–150` | Brødteksten henviser nu til `arr`, som pseudokoden. |
| `chapter15.tex:908–910` | Summen betegner nu alle indre løkkeiterationer på tværs af ydre løkkeiterationer; det præcise indre antal er `⌈log₂ n⌉` for `n≥1`. |
| `chapter14.tex:133` | Den strenge ulighed `n²<2ⁿ` gælder for heltal `n≥5`; ingen efterfølgende induktion skulle tilpasses. |
| `chapter14.tex:60` | Den ødelagte sætning er rettet og peger via `\autoref` på kapitlets indledning. |
| `chapter10.tex:715` | Den ydre parentes omkring “where/hvor u=…” er lukket. |
| `chapter10.tex:1253` | Definitionen forudsætter nu, at `f′` er differentiabel i `x`. |
| `chapter01.tex:276` | Det bogstavelige `{label:}`-argument er fjernet. |
| `chapter02.tex:61` | Pladserne efter det binære punktum er `2⁻¹`, `2⁻²`, … |
| `chapter02.tex:481,525,569,615` | Kolonnerne tælles nu fra LSB i begge udgaver. |
| `chapter06.tex:442` | Den afbrudte engelske sætning er fuldført og “examplifies” rettet til “exemplifies”; dansk var allerede hel. |
| `chapter09.tex:660` | Transponeringsreglen er henvist til som (d). |
| `chapter09.tex:199` | `B`-opstillingen har nu fire arraykolonner og særskilt `&` omkring `\cdots`. |
| `chapter08.tex:1242,1270` | Parametrene hedder nu `x₂,x₃` i begge formler. |
| `chapter08.tex:1404` | Den misvisende henvisning til sætningens sidste del er erstattet af en præcis overgang til korollaret. |
| `chapter11.tex:359` | Afslutningen henviser nu til bogens del, da kapitel 12–15 følger. |
| `chapter13.tex:390` | Den sande tredje identitet står nu under “absorptionslove og beslægtede forenklingsregler”. |
| `chapter13.tex:551` | Gates beskrives nu som opbygget af transistorer. |
| `concepts.tex:1289` | `\setcounter{enumi}{6}` er flyttet ind i `enumerate`, så kædereglen bliver punkt 7. |
| `concepts.tex:856` | Den ikkeeksisterende “matrix ovenfor” er erstattet af et selvstændigt 3×3/3×4-eksempel. |
| `concepts.tex:1302–1305` | Det gentagne display af potensreglen er fjernet. |
| `concepts.tex:678` | Første Bayes-lighed forudsætter nu både `P(A)>0` og `P(B)>0`. |
| `chapter09.tex:1263`, `concepts.tex:1200` | Nulvektoren bruger nu `\vect{0}`. |
| `chapter09.tex:1266`, `concepts.tex:1203` | “span/udspænder” er sat som verbum i teksten. |
| `figure/topographic-map.png` | Etiketten er rettet til “Hilly terrain” i den engelske PNG; kun 526 pixels i tekstfeltet er ændret. Dansk havde allerede en dansk etiket. |
| `chapter05.tex:24–46` | `B={3,4,5,6}` og `P(A\mid B)=2/4=1/2`; alle tal i løsningen er tilpasset. |
| `chapter00.tex:217` | Den tilsigtede advarsel mod at lægge tællere og nævnere sammen viser nu `(a+c)/(b+d)`. Begge viste ligheder er ugyldige generelt; rettelsen præciserer den typiske fejl. |
| `chapter10.tex:1079,1142–1158` | `f(2)=f(5)=1`; tekst, figurmarkering og billedtekst viser begge globale minimumspunkter. |
| `chapter15.tex:1276` | Loop6 har nu den eksakte geometriske sum og den gyldige øvre grænse `(log₂ n+1)(n+1)`. Den foreslåede gamle grænse var falsk for fx `n=5`. |
| `chapter14.tex:965` | Formlen viser forholdet `f(n)/g(n)=2sin(n)+3`; den følgende tekst konstaterer, at grænseværdien ikke findes. |
| `chapter14.tex:636,750` | Den selvmodsigende tilføjelse om “samme vækstrate” er fjernet. |
| `chapter14.tex:168` | Figuren tegner nu `log₂ x`, og titel, legendetekst og billedtekst bruger samme grundtal. |
| `chapter14.tex:282` | Eksemplet omtaler nu kun store O. |
| `chapter14.tex:9` | Notationen er nu `\mathcal{O}`. |
| `chapter06.tex:691` | Percentilteksten siger “på eller under” som definitionen. |
| `chapter06.tex:846–849` | Løftet om en senere forklaring af kurtosis er fjernet; den mangler fortsat med vilje efter brugerens valgmulighed. |
| `chapter03.tex:361`, `concepts.tex:408` | “Dually isomorphic/dualt isomorfe” blev først ændret til “isomorphic/isomorfe”; den senere præcisering til delmængdealgebra er registreret ovenfor. |
| `concepts.tex:1258` | Potensreglen har nu forbehold om, hvor den reelle potensfunktion er defineret og differentiabel. |
| `chapter13.tex:244` | Det engelske “since” er rettet til “although”; dansk havde allerede “selv om”. |
| `chapter12.tex:124` | Hypotenuse-eksemplet siger nu, at `√2` optræder som en længde, uden at udgive det for et irrationalitetsbevis. |
| `chapter01.tex:756,781` | Det engelske eksempel `log₅17` har nu label og `\autoref` som den danske udgave. |
| `chapter02.tex:100` | Den engelske binærbrøk er rettet til `0.1011₂` som den danske udgave. |
| `chapter05.tex:4` | Den engelske kapitelindledning siger nu “In this chapter”. |
| `chapter12.tex:195` | “GFC” er rettet til “GCF” i engelsk kilde. |
| `chapter15.tex:1402` | Den engelske afbrudte sætning er fuldført som “iterative binary search”. |
| `appendix01.tex:6` | `\unskip` efter `\For` fjerner et mellemrum før kommaet i engelsk kilde. |
