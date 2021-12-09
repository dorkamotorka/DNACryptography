# DNA Kriptografija

## Terminologija

- DNA (Deoksiribonukleinska kislina) je mulekula, ki je nosilka genetske informacije v vseh živih organizmih
- Nukleotid je osnovna enota DNA, ki je sestavljena iz sladkorja, dušikove baze in fosfatne skupine
- Kodon so trije pari nukleotidov (pari v dvojni vijačnici)


## Zapisovanje binarnih podatkov v DNA

Dandanes je zelo pomembno področje raziskovanja efektivno in zgoščeno shranjevanje podatkov. 
Pri tem ima DNA nit zelo velik potencial zaradi visoke zgoščenosti ter dolgoročnosti shrambe, vendar je pred končno uresničitvijo ideje potrebno odpraviti še kar nekaj težav kot so naprimer, počasni zapis in branje podatkov iz niti, visoke cena...
DNA nit je sestavljena iz štirih glavnih komponent: Adenin(A), Gvanin(G), Citozin(C) in Timin(T) s pomočjo katerih smo zakodirali binarne podatke v kombinacije le teh.
Kot pri vsakem izmed zapisov ali branju podatka obstaja možnost da pride do napake, kar velja tudi za DNA niti.
Ene izmed možnih napak so:
- Zamenjava baze (analogno se dogodi v električnih vezjih ti. bit-flip)
- Mutacija kodonov (Izbrisan ali dodan nukleotid, spremeni celotno sekvenco nukleotidov, kateri so po tri spadali h kodonom)

Temu primerno smo izbrali Huffmanovo enkodiranje, ki omogoča zanesljivejši zapis z manjšo verjetnostjo omenjenih napak in predstavlja de facto med standardi zapisov binarnih podatkov v DNA. 
Črki v angleški abecedi pripada dušikova baza oz. kombinacija le teh na podlagi frekvence/pogostosti črke.

![image](https://user-images.githubusercontent.com/48418580/145455912-35f58f66-00c9-4159-999d-deba0eb0a9a0.png)

DNA ima obliko dvojne vijačnice, pri čemer se dve mulekuli ovijeta druga okrog druge, pri čemer se dušikove baze vežejo v parih. Adenin se vedno pari s timinom in citozin vedno z gvaninom.
