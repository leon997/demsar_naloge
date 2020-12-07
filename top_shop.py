"""Modro	vodstvo	 tretje	 trgovine	za	drugim	vogalom	je	analiziralo	poslovanje	druge	 trgovine	in
odkrilo,	 da	 ima	 dolge	 vrste	 na	 blagajnah,	 to	 pa	 zato,	 ker	 morajo	 blagajniki	 prešteti	 izdelke,
preden	 lahko	 začnejo	 vnašati	 njihove	 cene.	 Zase	 je	 naročilo	 nov	 program,	 ki	 ne	 vpraša	 po
številu	izdelkov,	temveč	sprašuje	po	cenah	toliko	časa,	dokler	blagajnik	ne	vnese	ničle.
Cena artikla: 2
Cena artikla: 4
Cena artikla: 1
Cena artikla: 0
Vsota: 7.0"""

cena = int(input("Cena artikla: "))
sum = cena

while cena != 0:
    cena = int(input("Cena artikla: "))
    sum = sum + cena


print("Vsota: " + str(sum))
