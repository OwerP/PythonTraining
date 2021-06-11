"""
Napisz klasę `Zolw` z metodami `idz` i `obroc_sie`. Żółw ma jakieś położenie (wyrażone dwiema współrzędnymi) i jakieś ustawienie, czyli kurs (wyznaczony pojedyncza liczba).
Początkowe położenie podajemy konstruktorowi klasy, początkowy kurs to zawsze 0.
Metoda `obroc_sie ` powoduje obrót żółwia, czyli zmianę jego kursu.
Metoda `idz` powoduje przejście żółwia o określoną odległość.
Z klasy będzie się korzystać tak:

```python
z = Zolw(100, 100)
z.idz(50)

print(z) # ma sie wypisac: x=100, y=50

z.obroc_sie(90)
z.idz(50)
print(z) # ma sie wypisac: x=150, y=50
"""
import math


class Zolw():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0

    def idz(self, z: float):
        self.x += round(z * math.cos(self.direction / 360 * 2 * math.pi), 2)
        self.y += round(z * math.sin(self.direction / 360 * 2 * math.pi), 2)

    def obroc_sie(self, alfa):
        self.direction += alfa

    def __str__(self):
        return (f'x={self.x}, y={self.y}')


zolw = Zolw(100, 100)
zolw.idz(50)
print(zolw)
zolw.obroc_sie(90)
zolw.idz(50)
print(zolw)
zolw.obroc_sie(30)
zolw.idz(50)
print(zolw)
