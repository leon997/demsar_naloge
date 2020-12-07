"""Konkurenca	ne	spi.	Trgovina	za	vogalom	se	je	odločila	za	posebno	ponudbo:	kupec	lahko	kupi
toliko	izdelkov,	kolikor	želi.	Napiši	program,	ki	blagajnika	vpraša,	koliko	izdelkov	je	v	košarici,
nato	vpraša	po	cenah	teh	izdelkov	in	na	koncu	izpiše	vsoto.
Število izdelkov: 3
Cena artikla: 2
Cena artikla: 4.5
Cena artikla: 1.25
Vsota: 7.75"""


stevilo = int(input("Koliko izdelkov je v kosarici? "))
i = 0
sum = 0

while i < stevilo:
    cena = int(input("Cena artikla: "))
    sum = sum + cena
    i = i +1

print("Vsota: " + str(sum))