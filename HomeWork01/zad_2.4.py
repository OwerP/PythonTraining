"""
Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.

Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją i pełni w informatyce bardzo ważną rolę.
 Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024).
"""
from random import randint
liczba_losowana=randint(0,999)  #
#print (f"liczba wylosowana {liczba_losowana}")
counter = 0
while True:
    wartosc_uzytkownika = int(input('zgadnij co wylosowałem z zakresu 0 - 999: '))
    counter += 1
    if wartosc_uzytkownika > liczba_losowana:
        print (f"za dużo")
    elif wartosc_uzytkownika < liczba_losowana:
        print (f"za mało ")
    else:
        print(f"lgratulacje zgadłeś w {counter} próbie ")
        break


