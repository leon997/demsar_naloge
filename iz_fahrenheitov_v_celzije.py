"""Napiši	program,	ki	mu	uporabnik	vpiše		temperaturo	v	Fahrenheitovih	stopinjah, program	pa
jo	izpiše	v	Celzijevih.	Med	temperaturama	pretvarjamo	po	formuli	C	=	5/9	(F	– 32).
Za	potrebe	Američanov	napiši	še	program,	ki	računa	v	nasprotno	smer."""


def fahr_to_celz(fahr):
    celz = 5 / 9 * (fahr - 32)
    return celz

def celz_to_fahr(celz):
    fahr = celz * (9/5) + 32
    return fahr


print(fahr_to_celz(230))
print(celz_to_fahr(30))