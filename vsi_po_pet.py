"""V	 trgovini	 "Vsi	 po	 pet"	 morajo	 stranke	 vedno	 kupiti	 natanko	 pet	 artiklov.	 Za	 blagajne	 zato
potrebujejo	programsko	opremo,	ki	uporabnika	(blagajnika)	vpraša	po	petih	cenah;	ko	jih	le-ta
vnese,	program	izpiše	vsoto.
Cena artikla: 2
Cena artikla: 4.5
Cena artikla: 1
Cena artikla: 6
Cena artikla: 3
Vsota: 16.5"""

i = 0
sum = 0

while i < 5:
    cena = int(input("Vnesite ceno artikla: "))
    sum = sum + cena
    i = i + 1

print("Vsota: " + str(sum))