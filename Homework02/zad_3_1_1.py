
from Homework02.zad_3_1 import circle_field

promien = float(input("podaj promień koła:"))
print(f'pole koła o promieniu {promien} wynosi {circle_field(promien)} jednostek kwadratoowych ')

from Homework02.zad_3_1 import bmi
wzrost, masa = input('podaj odzielajac przecinkiem wzrost [m] i masę ciała[kg]: ').split(',')
try:
    wynik = bmi( float(masa),float(wzrost))
    print(wynik)
except ValueError:
    print('Niepoprawne dane')

from Homework02.zad_3_1 import miles_vs_km
wart_do_konwersji, kierunek_konwersji = input('podaj odzielajac przecinkiem wartosc do konwersji w [m lub mile]  oraz kierunek konwersji [m2k lub k2m]: ').split(',')
wynik = miles_vs_km(float(wart_do_konwersji), kierunek_konwersji)

if kierunek_konwersji == 'm2k':
    print (f"{wart_do_konwersji} mil to {wynik} km")
else:
    print (f"{wart_do_konwersji} km to {wynik} mil")