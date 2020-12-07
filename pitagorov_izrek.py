"""Napiši	 program,	 ki	 uporabnika	 vpraša	 po	 dolžinah	 katet	 pravokotnega	 trikotnika	 in	 izpiše
dolžino	 hipotenuze. (Da	 ponagajamo	 pokojnemu	 prof.	 Križaniču,	 ki	 je	 sovražil	 dlakocepce,
dodajmo	"dolžino	hipotenuze	taistega	trikotnika".)"""

import math

kateta1 = input("Dolžina prve katete: ")
kateta2 = input("Dolžina druge katete: ")


def pitagorov_izrek(kateta1, kateta2):
    hip = math.sqrt(int(kateta1) ** 2 + int(kateta2) ** 2)
    return hip


print(pitagorov_izrek(kateta1, kateta2))