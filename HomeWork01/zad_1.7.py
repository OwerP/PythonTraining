"""
Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena. Wyświetl odpowiedni komunikat.

Przykład:
Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10

Za ziemniaki, który chcesz kupić, zapłacisz 50 zł
"""

towar= input('o chcesz kupić? - ')
cena_towaru= float(input('Podaj cenę towaru - [PLN]: '))
ilosc_towaru= float(input('Podaj ilość towaru - : '))
print (f"Za {towar}, który chcesz kupić, zapłacisz {round(cena_towaru*ilosc_towaru,2)} zł")
