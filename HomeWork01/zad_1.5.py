"""
Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.

Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).

Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:

```
import math

x = math.sqrt(10)
```
"""
import math

a, b, c = input('podaj odzielajac przecinkiem wymiary trójkata: ').split(',')
a, b, c = float(a), float(b), float(c)
if a + b > c and b + c > a and a + c > b:
    p = (a + b + c) / 2
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print (f"Pole tego trójkata wynosi {pole}")
else:
    print("to nie jest trójkąt")
