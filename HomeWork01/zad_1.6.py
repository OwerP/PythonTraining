"""
Założenia:
	- 0-6   - wiek przedszkolny - cena biletu: 0
	- 7-17  - wiek szkolny      - cena biletu: 2.28
	- 18-64 - wiek dorosły      - cena biletu: 3.80
	- +65   - wiek emerytalny   - cena biletu: 1.90

Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.

Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.
"""

wiek, ilosc_biletow = input('podaj odzielajac przecinkiem wiek [lata] i ilosc ilość biletów[sztuki]: ').split(',')
wiek = int(wiek)
ilosc_biletow = int(ilosc_biletow)
cena_biletu = 0
koszt = 0
if wiek <= 6.0:
    cena = 0
elif 6 < wiek <= 17:
    cena = 2.28
elif 17 < wiek <= 64:
    cena = 3.8
else:
    cena = 1.9
koszt = round(ilosc_biletow * cena, 2)

print(f"Koszt biletów wynosi {round(koszt,2)} ")
