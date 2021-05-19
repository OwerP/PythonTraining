"""
Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza, ile trzeba zapłacić. Zasady są takie:

- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
	- 200 zł za noc, jeśli nocują jedną noc
	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki

Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki, czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.
"""

wiek, ilosc_nocy = input('podaj odzielajac przecinkiem wiek [lata] i ilosc nocy w hotelu[dni]: ').split(',')
wiek = int(wiek)
ilosc_nocy = int(ilosc_nocy)
koszt = 0
if wiek < 18.0:
    print(f"Nieletni, koszt pobytu {100 * ilosc_nocy}")
else:
    if ilosc_nocy == 1:
        koszt = 200
    elif 1 < ilosc_nocy < 5:
        koszt = 180 * ilosc_nocy
    else:
        koszt = 150 * ilosc_nocy

    if wiek > 65:
        koszt = 0.9 * koszt

    print(f"Koszt pobytu w hotelu wynosi {round(koszt,2)} ")
