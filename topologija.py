"""Napiši	 program	 za	 izračun	 dolžine	 strela	 s	 topom	 (ki	 brez	 trenja	 izstreljuje	 točkaste	 krogle	 v
brezzračnem	 prostoru,	 a	 pustimo	 trivio).	 Program	 od	 uporabnika	 ali	 uporabnice	 zahteva,	 da
vnese hitrost	 izstrelka	 (to	 je,	 omenjene	 točkaste	 krogle)	 in	 kot,	 pod	 katerim	 je	 izstreljen.
Program	naj	izračuna	in	izpiše,	kako	daleč	bo	letela krogla.
Pomoč	za	fizično	nebogljene:	s =	v
2 sin(2φ)/g,	kjer	je	s razdalja,	v hitrost	izstrelka,	φ je	kot,	g pa
osma	črka	slovenske	abecede.
Preveri	tole:	krogla	leti	najdalj,	če	jo	izstrelimo	pod	kotom	45	stopinj.	Poskusi,	kako	daleč	gre
pod	kotom	45	in	kako	daleč	pod	46	stopinj	-- po	45	mora	leteti	dlje.	Preveri	tudi	kot	50	stopinj:
če	pod	tem	kotom	leti	nazaj	(razdalja	je	negativna),	si	ga	gotovo	nekje	polomil."""

import math

hitrost = input("Vnesite hitrost izstrelka: ")
kot = input("Vnesite še kot pod katerim je bil izstreljen: ")


def izracun_dolzine(hitrost, kot):
    dolzina = int(hitrost) ** 2 * (math.sin(2 * int(kot))) / 10
    return dolzina


print(izracun_dolzine(hitrost, kot))