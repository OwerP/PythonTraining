"""
Zakładamy, że 1 ludzki rok, to 5 lat psich.  < to chyba błąd

Zakładamy, że 1 ludzki psi, to 5 lat ludzkich.
Za pomocą konsoli wczytaj imię i wiek psa.
Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.

Przykład:
Podaj imię psa - Burek
Podaj wiek psa - 3

Gdyby Burek był człowiekiem, miałby 15 lat.
"""

imie_psa= input('podaj imię psa: ')
wiek_psa= float(input('podaj wiek psa [lata]: '))

print (f"gdyby {imie_psa} był człowiekiem to miałby {5* wiek_psa} lat")
