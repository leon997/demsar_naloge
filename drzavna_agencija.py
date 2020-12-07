"""Zaradi	 poplave	 sumljivih	 trgovin	 za	 vogali	 se	 je	 Državna	 agencija	 za	 varstvo	 potrošnikov
odločila	nadzorovati	poprečne	cene	izdelkov	v	košaricah	strank.	Popravi	zadnji	ali	predzadnji
program	tako,	da	bo	izpisal	tudi	poprečno	ceno.
OSNUTEK
Cena artikla: 2
Cena artikla: 4
Cena artikla: 1
Cena artikla: 0
Vsota: 7
Poprečna cena: 2.33333333333
Ne	vznemirjaj	se	zaradi	grdega	izpisa	cene;	državni	uradniki	so	natančni	in	želijo	vedeti	vse	do
zadnje	decimalke!"""


cena = int(input("Cena artikla: "))
sum = cena
stevc = 0

while cena != 0:
    cena = int(input("Cena artikla: "))
    sum = sum + cena
    stevc = stevc + 1


povprecje = sum / stevc

print("Vsota: " + str(sum))
print("Povprečna cena: " + str(povprecje))