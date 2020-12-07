"""Napiši program,	ki	izpiše	vse	delitelje	podanega	števila.
Vpiši število: 12345
1
3
5
15
823
2469
4115
12345"""


stevilo = int(input("Vpisi stevilo: "))
i = 1

while i < stevilo:
    p = stevilo / i
    if isinstance(p, int):
        print(i)
    i = i + 1