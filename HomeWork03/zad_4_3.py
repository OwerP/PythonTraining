"""
Stwórz klasę `Pociag`. Klasa niech ma dwa atrybuty: predkość (początkowa wartość to 10) i ilosc_paliwa (początkowa wartość to 1000).

Dodaj do klasy `Pociag` metode `opis`. Ta metoda niech zwraca napis o treści "Moja predkość to (ileś tam).
Mam jeszcze (ileś tam) litrów paliwa." Dodatkowo zaimplementuj metodę `__str__`.

Dodaj metode `przyspiesz`. Ta metoda niech przyjmuje jeden argument mówiący, o ile ma zwiekszyć się prędkość.
Ta metoda niech zwiększa predkość pociągu o tyle, ile jest powiedziane w argumencie.
I niech zmniejsza ilość paliwa o: `(nowa predkosc - stara_predkosc) * (stara predkosc / 100)`.

Niech nie da się jednorazowo zwiększyć prędkości o więcej niż 75% (jeśli ktoś spróbuje tak zwiększyć prędkość, prędkość niech pozostaje po prostu bez zmian).
Niech nie da sie zwiększyć prędkości, jeśli pociąg nie ma juz paliwa (jeśli ktoś spróbuje zwiększyć prędkość, kiedy nie ma paliwa, prędkość niech pozostaje po prostu bez zmian).

Przetestuj swoje rozwiązanie i napisz testy, w których:
- zwiększysz prędkość pociągu o 5 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 20 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 8 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 10 km/h i wypisze jego opis
"""
import pytest

class Pociag:
    def __init__(self):
        self.speed=10
        self.fuel_level = 1000

    def przyspiesz(self, speed: int):
        last_speed=self.speed
        last_fuel_level = self.fuel_level

        self.speed +=speed
        self.fuel_level -= (self.speed - last_speed) * last_speed / 100
        if (round(100*(self.speed-last_speed)/last_speed,1)>75 or self.fuel_level<0 or speed < 0):
            self.speed=last_speed
            self.fuel_level=last_fuel_level


    def __str__(self):
        return f'Moja predkość to {self.speed}. Mam jeszcze {self.fuel_level} litrów paliwa.'

    def opis(self):
        return self.__str__()

# pociag = Pociag()
# pociag.przyspiesz(5)
# pociag.przyspiesz(20)
# pociag.przyspiesz(8)
# pociag.przyspiesz(10)
# print (pociag.opis())

def test_negative_range():
    pociag = Pociag()
    pociag.przyspiesz(-10)
    assert pociag.opis() == 'Moja predkość to 10. Mam jeszcze 1000 litrów paliwa.'

def test_przyspiesz_5():
    pociag = Pociag()
    pociag.przyspiesz(5)
    assert pociag.opis() == 'Moja predkość to 15. Mam jeszcze 999.5 litrów paliwa.'

def test_przyspiesz_5_20():
    pociag = Pociag()
    pociag.przyspiesz(5)
    pociag.przyspiesz(20)
    assert pociag.opis() == 'Moja predkość to 15. Mam jeszcze 999.5 litrów paliwa.'

def test_przyspiesz_5_20_8():
    pociag = Pociag()
    pociag.przyspiesz(5)
    pociag.przyspiesz(20)
    pociag.przyspiesz(8)
    assert pociag.opis() == 'Moja predkość to 23. Mam jeszcze 998.3 litrów paliwa.'

def test_przyspiesz_5_20_8_10():
    pociag = Pociag()
    pociag.przyspiesz(5)
    pociag.przyspiesz(20)
    pociag.przyspiesz(8)
    pociag.przyspiesz(10)
    assert pociag.opis() == 'Moja predkość to 33. Mam jeszcze 996.0 litrów paliwa.'