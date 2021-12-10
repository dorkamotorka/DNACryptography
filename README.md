# DNA Kriptografija

## Biologija

### DNA (Deoksiribonukleinska kislina) 

je mulekula, ki je nosilka genetske informacije v vseh živih organizmih. Ima obliko dvojne vijačnice, pri čemer se dve mulekuli ovijeta druga okrog druge, pri čemer se dušikove baze vežejo v parih. Adenin se vedno pari s timinom in citozin vedno z gvaninom.

### Osnovni elementi

**Nukleotid** je osnovna enota DNA, ki je sestavljena iz sladkorja, dušikove baze in fosfatne skupine.
**Kodon** so trije pari nukleotidov (pari v dvojni vijačnici).
Osnovni elementi, ki jih bomo uporabljali (analogno iz digitalnih vezjih) kot en-bit informacije so dušikove baze: Adenin(A), Gvanin(G), Citozin(C) in Timin(T).

## mRNA

je mulekula, ki širi oz. posreduje genetsko informacijo med DNA in beljakovinami. 
Konceptno deluje tako, da v procesu prepisovanja(iz ene izmed verig dvojne vijačnice) mRNA tvori enoverižno molekulo, ki predstavlja komplement/inverz prebrane verige.
Komplementi dušikovih baz so sledeči:
- Gvanin -> Citozin
- Adenin -> Timin
- Timin -> Uracil

Torej če imamo sledečo dvojno vijačnico in mRNA, ki prebira:

    A G G G A (zgornja veriga)
    | | | | | (vez med paroma)  DNA
    T C C C T (spodnja veriga)
    ----------
    U G G G U (mRNA, ki prebere spodnjo verigo) 

## Zapisovanje binarnih podatkov v DNA

Dandanes je zelo pomembno področje raziskovanja efektivno in zgoščeno shranjevanje podatkov. 
Pri tem ima DNA nit zelo velik potencial zaradi visoke zgoščenosti ter dolgoročnosti shrambe, vendar je pred končno uresničitvijo ideje potrebno odpraviti še kar nekaj težav kot so naprimer, počasni zapis in branje podatkov iz niti, visoke cena...
Kot pri vsakem izmed zapisov ali branju podatka obstaja možnost da pride do napake( zaradi spontane napake, UV žarki, toplota itd.), kar velja tudi za DNA niti.
Ene izmed možnih napak so:
- Zamenjava baze (analogno se dogodi v električnih vezjih ti. bit-flip)
- Mutacija kodonov (Izbrisan ali dodan nukleotid, spremeni celotno sekvenco nukleotidov, kateri so po tri spadali h kodonom)

Obstaja možnost, da podatke v DNA enkodiramo tako, da si izberemo preslikavo med dušikovo bazo(nukleotid) in kombinacijo bitov. 
Naprimer:
   
    Adenin(A) <=> 00
    Gvanin(A) <=> 01
    Citozin(A) <=> 10
    Timin(A) <=> 11
    
In temu primerno zapišemo podatke v DNA, vendar izkaže se da je pogostost napak, ki se lahko pripetijo določenemu tipu nukleotida je večja ali manjša od preostalih. Upoštevajoč to lastnost lahko v primeru teksta, pogostejše črke kot so (e,a,t ..) zapisujemo v kombinaciji dušikovih baz, ki bolj zanesljive oz. je manjša verjetnost da pride do napak in s tem izboljšamo zanesljivost zapisa, branja in hrambe podatkov.
To lastnost izkorišča Hufmanovo enkodiranje, ki ASCII vrednostim pogostejšim črkam pripisuje zanesljivejše kombinacije dušikovih baz.
Tabela prestavlja preslikava:

![image](https://user-images.githubusercontent.com/48418580/145455912-35f58f66-00c9-4159-999d-deba0eb0a9a0.png)

Pomembno je dodati da se vsak zapis oz. začetek DNA začne z start kodonom, ki je običajno kombinacija ATG dušikovih baz, pri čemer konec zapisa DNA naznanimo z stop kodonom, ki bo v našem primeru TAG kombinacija dušikovih baz. 
