"""Napiši	program,	ki	mu	uporabnik	vpiše	niz	in	pove,	koliko	črk	a	je	v	njem."""

niz = input("Vpišite niz: ")
count = 0

for i in niz:
    if i.isalpha():
        count += 1

print(count)