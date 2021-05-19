"""
Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
"""
from random import randint
liczba_losowana1=randint(0,99)  #
liczba_losowana2=randint(0,99)  #
print (f"liczba nr1 {liczba_losowana1} liczba nr2 {liczba_losowana2} ")
suma= liczba_losowana1 + liczba_losowana2
counter = 0
while True:
    wartosc_uzytkownika = int(input('zgadnij sumę w/w liczb: '))
    counter += 1
    if wartosc_uzytkownika != suma:
        print (f"próbuj jeszcze raz ")
    else:
        print(f"gratulacje, zgadłeś w {counter} próbie ")
        break


