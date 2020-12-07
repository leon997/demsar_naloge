"""Ploščino	 trikotnika	 s	 stranicami	 a,	 b	 in	 c	 lahko	 izračunamo	 po	 Heronovem	 obrazcu:
p = s(s − a)(s −b)(s − c) ,	kjer	je	s velikost	polobsega,	s = (a + b + c)/ 2.	Napiši	program,
ki	uporabnika	vpraša	po	dolžinah	stranic	in	izpiše	(njegovo)	ploščino.
Program	naj	popazi	na	nepravilne	podatke.	Preveri,	kaj	se	zgodi,	če	uporabnik	zatrdi,	da	ima
trikotnik	stranice	1,	2	in	5.	Takšnega	trikotnika	pač	ni	(krajši	stranici	se	ne	stakneta!)	.	Program
naj	v	tem	primeru	pozove	uporabnika	k	resnosti."""

import math


stranica1 = int(input("Dolzina prve stranice: "))
stranica2 = int(input("Dolzina druge stranice: "))
stranica3 = int(input("Dolzina tretje stranice: "))

if stranica1 >= stranica2 and stranica1 >= stranica2:
    if stranica1 >= stranica2 + stranica3:
        print("Dej zresni se!")
elif stranica2 >= stranica1 and stranica2 >= stranica3:
    if stranica2 >= stranica1 + stranica3:
        print("Dej zresni se!")
elif stranica3 >= stranica1 and stranica3 >= stranica2:
    if stranica3 >= stranica1 + stranica2:
        print("Dej zresni se!")


s = (stranica1 + stranica2 + stranica3) / 2

def ploscina(stranica1, stranica2, stranica3, s):
    p = math.sqrt(s*(s-stranica1)*(s-stranica2)*(s-stranica3))
    return p


print(ploscina(stranica1, stranica2, stranica3, s))