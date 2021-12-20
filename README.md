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

tRNA je mulekula, ki prevaja mRNA v eno izmed aminokislin. Prevajanje je enako komplementu dušikovih baz, ki skupaj tvorijo enoverižno mulekulo.
Komplementi dušikovih baz so sledeči:
- Gvanin --> Citozin
- Citozin --> Gvanin
- Adenin --> Uracil
- Uracil --> Adenin

tRNA je nazaj pretvorimo v DNA mulekulo tako da Uracil nadomestimo z Timinom.

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

Zaradi same narave besedil in procesa enkodiranja, ki eni črki lahko pridedi kombinacijo več dušikovih baz, je potrebno pred enkriptiranjem poskrbeti da je dolžina DNA sekvence deljiva z 4. 
To pa zato, ker vsaki bazi pripadata dva bita(torej dolžnina sekvenco bitov bo/mora biti deljiva z 8) in ker bomo uporabljali 8-bitne substitucijske škatle (S-box). 
Če pogoju besedilo ne zadosti na koncu besedila dopolnimo verigo z Adenini(A-ji).

## SP Mreža (ang. SPN)

Substitucijska-Permutacijska mreža krajše SP Mreža je osnovna komponenta nekaterih glavnih enkripcijskih algoritmov kot so AES, DES itd. Glavne lastnosti so predvsem enostavnost, hitrost ter učinkovist. 
Kot že ime pove bo sestavljena iz S-škatel (substitucija) in P-škatel(permutacija) ter XOR operacije z ključem-kroga.

![img](spn.png)

## S-škatle

Za substitucijsko škatlo obstaja standard, ki zagotovalja zadostno difuzijo ter konfuzijo teksta. Temu primerno vzamemo kar enako tabelo kot za AES, le da je priredimo za substitucijo z dušikovimi bazami:



## P-škatle

V našem primeru bodo permutacijske škatle permutirale vhodne bite s pomočjo mRNA in tRNA operacij(opisane zgoraj) ter pretvorbe nazaj v DNA sekvenco. 
Če povzamemo iz opisa operacij, za posamezno bazo to pomeni:

	T --> U --> A --> A
	A --> A --> U --> T
	C --> C --> G --> G
	G --> G --> C --> C

TODO: v enem izmed paperjev se je shiftalo po vsaki rundi v desno(koncni rata prvi itd.)

![image](https://user-images.githubusercontent.com/48418580/146830900-8b92dfc9-142c-4deb-bdea-be5ee96f8756.png)

## XOR z ključem-kroga

Preden naredimo XOR z ključem-kroga pretvorimo posamezno bazo v bite na sledeči način:

    Adenin(A) <=> 00
    Gvanin(G) <=> 01
    Citozin(C) <=> 10
    Timin(T) <=> 11

TODO: Dolžina ključa == dolžina text-a

## Generacija ključev-kroga

Iz primarnega ključa, ki ga uporabnik izbere se zgenerira toliko ključev-kroga kolikor je krogov enkripcije SP mreže.

TODO

## Test difuzije (spremeniš en bit inputa in so output biti vsi povsem drugačni)
