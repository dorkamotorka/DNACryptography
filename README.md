# DNA Kriptografija

## Biologija

### DNA (Deoksiribonukleinska kislina) 

je mulekula, ki je nosilka genetske informacije v vseh živih organizmih. Ima obliko dvojne vijačnice, pri čemer se dve mulekuli ovijeta druga okrog druge, pri čemer se dušikove baze vežejo v parih. Adenin se vedno pari s timinom in citozin vedno z gvaninom.

### Osnovni elementi

**Nukleotid** je osnovna enota DNA, ki je sestavljena iz sladkorja, dušikove baze in fosfatne skupine.
**Kodon** so trije pari nukleotidov (pari v dvojni vijačnici).
Osnovni elementi, ki jih bomo uporabljali (analogno iz digitalnih vezjih) kot en-bit informacije so dušikove baze: Adenin(A), Gvanin(G), Citozin(C) in Timin(T).

## mRNA

je mulekula, ki širi oz. prepisuje genetsko informacijo iz DNA. 
Konceptno deluje tako, da v procesu prepisovanja(iz ene izmed verig dvojne vijačnice) mRNA tvori enoverižno molekulo, pri čemer Timin nadomesi Uracilom, preostanek prebrane verige ostane enak.
Torej če imamo sledečo dvojno vijačnico in mRNA, ki prebira:

    A G G G A (zgornja veriga)
    | | | | | (vez med paroma)  DNA
    T C C C T (spodnja veriga)
    ----------
    U C C C U (mRNA, ki prebere spodnjo verigo) 

## tRNA

tRNA je mulekula, ki prevaja mRNA v eno izmed aminokislin. 
Vsaka tRNA molekula ima tri nukleotide skupaj imenovane antikodon, in cilj prevajanje je da tRNA se poveže v mRNA s takšno kombinacijo nukleotidov, ki bo ravno komplement nukleotidov tRNA-ja in če takšna kombinacija nukleotidov obstaja bo ta ista tRNA omogočila prevod kodona mRNA v aminokislino. 
Torej prevod celotne mRNA verige je enako komplementu dušikovih baz, ki nato skupaj tvorijo enoverižno mulekulo.
Komplementi dušikovih baz so sledeči:

	Gvanin --> Citozin
	Citozin --> Gvanin
	Adenin --> Uracil
	Uracil --> Adenin

tRNA je nazaj pretvorimo v DNA mulekulo tako da Uracil nadomestimo z Timinom.

Tabela prevoda tRNA v aminokislino:

![image](https://user-images.githubusercontent.com/48418580/146944466-66d331d4-eed5-4e10-ae88-bfb2acaf29ec.png)

## Zapisovanje binarnih podatkov v DNA

Dandanes je zelo pomembno področje raziskovanja efektivno in zgoščeno shranjevanje podatkov. 
Pri tem ima DNA nit zelo velik potencial zaradi visoke zgoščenosti ter dolgoročnosti shrambe, vendar je pred končno uresničitvijo ideje potrebno odpraviti še kar nekaj težav kot so naprimer, počasni zapis in branje podatkov iz niti, visoke cena...
Kot pri vsakem izmed zapisov ali branju podatka obstaja možnost da pride do napake( zaradi spontane napake, UV žarki, toplota itd.), kar velja tudi za DNA niti.
Ene izmed možnih napak so:
- Zamenjava baze (analogno se dogodi v električnih vezjih ti. bit-flip)
- Mutacija kodonov (Izbrisan ali dodan nukleotid, spremeni celotno sekvenco nukleotidov, kateri so po tri spadali h kodonom)

Raziskave so pokazale, da je pogostost napak, ki se lahko pripetijo določenemu tipu nukleotida je večja ali manjša od preostalih. Upoštevajoč to lastnost lahko v primeru teksta, pogostejše črke kot so (e,a,t ..) zapisujemo v kombinaciji dušikovih baz, ki bolj zanesljive oz. je manjša verjetnost da pride do napak in s tem izboljšamo zanesljivost zapisa, branja in hrambe podatkov.
To lastnost izkorišča Hufmanovo enkodiranje, ki ASCII vrednostim pogostejšim črkam pripisuje zanesljivejše kombinacije dušikovih baz.
Tabela prestavlja preslikava:

![image](https://user-images.githubusercontent.com/48418580/145455912-35f58f66-00c9-4159-999d-deba0eb0a9a0.png)

   
Pomembno je dodati da se vsak zapis oz. začetek DNA začne z start kodonom, ki je običajno kombinacija ATG dušikovih baz, pri čemer konec zapisa DNA naznanimo z stop kodonom, ki bo v našem primeru TAG kombinacija dušikovih baz. 

## Padding 

Zaradi same narave besedil in procesa Huffmanovega enkodiranja, ki eni črki lahko pridedi kombinacijo več dušikovih baz, je potrebno pred enkriptiranjem poskrbeti da je dolžina DNA sekvence posameznega bloka enaka 32. 
To pa zato, ker vsaki bazi pripadata dva bita(torej dolžnina sekvence bitov bo enaka 64) in ker bomo uporabljali 8-bitne substitucijske škatle (S-box). 
Če pogoju besedilo ne zadosti na koncu besedila dopolnimo verigo z Citozinom(C), saj so raziskave pokazale da je le ta najbolj odporen na spontane genske napake [1].

## SP Mreža (ang. SPN)

Substitucijska-Permutacijska mreža krajše SP Mreža je osnovna komponenta nekaterih glavnih enkripcijskih algoritmov kot so AES, DES itd. Glavne lastnosti so predvsem enostavnost, hitrost ter učinkovist. 
Kot že ime pove bo sestavljena iz S-škatel (substitucija) in P-škatel(permutacija) ter XOR operacije z ključem-kroga.

![img](spn.png)

## Rijndael S-škatle

Za substitucijsko škatlo obstaja standard, ki zagotavlja zadostno difuzijo ter konfuzijo teksta. Temu primerno vzamemo kar enako tabelo kot za AES, le da je priredimo za substitucijo z dušikovimi bazami:

|    | AA   | AG   | AC   | AT   | GA   | GG   | GC   | GT   | CA   | CG   | CC   | CT   | TA   | TC   | TG   | TT   |
|----|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| AA | GCAT | GTTA | GTGT | GTCT | TTAC | GCCT | GCTT | TAGG | ATAA | AAAG | GCGT | ACCT | TTTG | TCGT | CCCT | GTGC |
| AG | TACC | CAAC | TACG | GTTC | TTCC | GGCG | GAGT | TTAA | CCTC | TCGA | CCAC | CCTT | CGTA | CCGA | GTAC | TAAA |
| AC | CTGT | TTTC | CGAT | ACGC | ATGC | ATTT | TTGT | TATA | ATGA | CCGG | TGGG | TTAG | GTAG | TCCA | ATAG | AGGG |
| AT | AAGA | TAGT | ACAT | TAAT | AGCA | CGGC | AAGG | CGCC | AAGT | AGAC | CAAA | TGAC | TGCT | ACGT | CTAC | GTGG |
| GA | AACG | CAAT | ACTA | AGCC | AGCT | GCTG | GGCC | CCAA | GGAC | ATCT | TCGC | CTAT | ACCG | TGAT | ACTT | CAGA |
| GG | GGAT | TCAG | AAAA | TGTC | ACAA | TTTA | CTAG | GGCT | GCCC | TACT | CTTG | ATCG | GACC | GATA | GGCA | TATT |
| GC | TCAA | TGTT | CCCC | TTCT | GAAT | GATC | ATAT | CAGG | GAGG | TTCG | AAAC | GTTT | GGAA | ATTA | CGTT | CCCA |
| GT | GGAG | CCAT | GAAA | CATT | CGAC | CGTC | ATCA | TTGG | CTTA | CTGC | TCCC | ACAG | AGAA | TTTT | TTAT | TCAC |
| CA | CTTC | AACT | AGAT | TGTA | GGTT | CGGT | GAGA | AGGT | TAGA | CCGT | GTTG | ATTC | GCGA | GGTC | AGCG | GTAT |
| CG | GCAA | CAAG | GATT | TCTA | ACAC | ACCC | CGAA | CACA | GAGC | TGTG | CTCA | AGGA | TCTG | GGTG | AACT | TCCT |
| CC | TGAA | ATAC | ATCC | AACC | GACG | AAGC | ACGA | GGTA | TAAC | TCAT | CCTA | GCAC | CGAG | CGGG | TGGA | GTCG |
| CT | TGGT | TACA | ATGT | GCTC | CATC | TCGG | GATG | CCCG | GCTA | GGGC | TTGA | TGCC | GCGG | GTCC | CCTG | AACA |
| TA | CTCC | GTCA | ACGG | ACTG | AGTA | CCGC | CTGA | TAGC | TGCA | TCTC | GTGA | AGTT | GACT | CTTC | CACT | CACC |
| TC | GTAA | ATTG | CTGG | GCGC | GACA | AAAT | TTGC | AATG | GCAG | ATGG | GGGT | CTCG | CAGC | TAAG | AGTC | CGTG |
| TG | TGAG | TTCA | CGCA | AGAG | GCCG | TCCG | CATG | CGGA | CGCT | AGTG | CAGT | TGCG | TATG | GGGG | ACCA | TCTT |
| TT | CATA | CCAG | CACG | AATC | CTTT | TGGC | GAAC | GCCA | GAAG | CGCG | ACTC | AATT | CTAA | GGGA | CTCT | AGGC |

## P-škatle

V našem primeru bodo permutacijske škatle permutirale vhodne bite s pomočjo mRNA in tRNA operacij(opisane zgoraj) ter pretvorbe nazaj v DNA sekvenco. 
Če povzamemo iz opisa operacij, za posamezno bazo to pomeni:

	T --> U --> A --> A
	A --> A --> U --> T
	C --> C --> G --> G
	G --> G --> C --> C

S pomočjo testa difuzije smo ugotovili da operaciji mRNA in tRNA ne zagotoviti zadovoljive enkripcije, zatorej smo le to izboljšali s pomočjo standarnega 64-bitnega P-boxa:

![image](https://user-images.githubusercontent.com/48418580/147093232-e3b225f2-db53-4c76-8a35-a6cc8120e8c7.png)

In njen inverz:

![image](https://user-images.githubusercontent.com/48418580/147093280-06613aba-caf9-4aa9-afdd-4ea7b52d753d.png)

Operacija transkripcije (s pomočjo mRNA) in translacije (s pomočjo tRNA) vizualizirana:

![image](https://user-images.githubusercontent.com/48418580/146830900-8b92dfc9-142c-4deb-bdea-be5ee96f8756.png)

## XOR z ključem-kroga

Preden naredimo XOR z ključem-kroga pretvorimo posamezno bazo v bite na sledeči način:

    Adenin(A) <=> 00
    Gvanin(G) <=> 01
    Citozin(C) <=> 10
    Timin(T) <=> 11

Nato 64-bitni tekst in 64-bitni ključ-kroga XOR-amo ter rezultat pretvorimo nazaj v dušikove baze.

## Generacija ključev-kroga

Iz primarnega ključa, ki ga uporabnik izbere se zgenerira toliko ključev-kroga kolikor je krogov enkripcije SP mreže.

TODO

## Test difuzije 

Sprememba ene izmed črke vhodnega teksta, bi morala vplivati na vse vrednosti izhoda.

TODO

## References

[1] https://web.stanford.edu/~kaleeg/chem32/biopol/
