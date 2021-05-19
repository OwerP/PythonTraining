"""
Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`.
Np. dla parametru 3 powinno się wypisać:

```
    *
  * * *
* * * * *
```
"""
ilosc_wierszy = int(input('wielkość choinki w wierszach: '))

for i in range(0, ilosc_wierszy):
    for k in range(2*ilosc_wierszy -2*(i+1), 0, -1):
        print(' ', end='')
    for j in range(0,2*i):
        print('*', end='')
        print(' ', end='')
    print('*', end='')
    print()

