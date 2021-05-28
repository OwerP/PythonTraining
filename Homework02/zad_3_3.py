"""
Stwórz następujące funkcje.
Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.

```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```

- `suma(liczby)` - zwraca sumę liczb z listy `liczby` - postaraj się nie używać funkcji `sum` wbudowanej w pythona
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby` - postaraj się nie używać funkcji `max` wbudowanej w pythona
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
- `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma nie.

"""
import pytest


def suma(list_of_values: list) -> float:
    """
    - `suma(liczby)` - zwraca sumę liczb z listy `liczby` - postaraj się nie używać funkcji `sum` wbudowanej w pythona
    :param list_of_values: ista wartości z których ma być obliczona suma
    :return: suma liczb z listy
    """
    if len(list_of_values) > 0:
        sum_ = 0
        for value in list_of_values:
            sum_ += value
        return round(sum_, 2)
    else:
        raise ValueError("list of arguments cannot be empty")


def srednia(list_of_values: list) -> float:
    """
    - `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
    :param list_of_values: lista wartości z których ma być wuliczona średnia
    :return: średnia z liczb z listy
    """
    if len(list_of_values) > 0:
        sum_ = 0
        for value in list_of_values:
            sum_ += value
        return round(sum_ / len(list_of_values),2)
    else:
        raise ValueError("list of arguments cannot be empty")


def max_(list_of_values: list) -> float:
    """
     `max(liczby)` – zwraca największą wartość z listy `liczby` - postaraj się nie używać funkcji `max` wbudowanej w pythona
    :param list_of_values: lista wartości z których ma być wybrany max
    :return: wartość maxymalna z listy
    """

    list_of_values.sort(reverse=True)
    return float(list_of_values[0])


def diff_max_min(list_of_values: list) -> float:
    """
    `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
    :param list_of_values: lista wartości z których ma być wybrana róznica  max i min
    :return: wartość maxymalna - minimalna z listy
    """

    list_of_values.sort(reverse=True)
    if len(list_of_values) > 0:
        return list_of_values[0] - float(list_of_values[len(list_of_values) - 1])
    else:
        return 0


def print_bigger(list_of_values: list, x: float) -> list:
    """
     wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
    :param list_of_values: lista wartości z których ma być wybrana
    :param x: wartość progowa
    :return: lista wartości większych niż progowe
    """
    list_filtered_result = list(filter(lambda y: y > x, list_of_values))
    return list_filtered_result


def first_bigger(list_of_values: list, x: float):
    """
     zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
    :param list_of_values: lista wartości z których ma być wybrana
    :param x: wartość progowa
    :return: lpierwsza większa niż  progowe
    """
    list_filtered_result = list(filter(lambda y: y > x, list_of_values))
    if len(list_filtered_result) == 0:
        return None
    else:
        return list_filtered_result[0]


def sum_bigger(list_of_values: list, x: float):
    """
    suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
    :param list_of_values: lista wartości z których ma być wybrana
    :param x: wartość progowa
    :return: suma większych niż  progowe
    """
    list_filtered_result = list(filter(lambda y: y > x, list_of_values))
    if len(list_filtered_result) > 0:
        sum_ = 0
        for value in list_filtered_result:
            sum_ += value
        return sum_
    else:
        raise ValueError("list of arguments cannot be empty")


def no_of_bigger(list_of_values: list, x: float):
    """
     `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
    :param list_of_values: lista wartości z których ma być wybrana
    :param x: wartość progowa
    :return: liczba większych niż  progowe
    """
    list_filtered_result = list(filter(lambda y: y > x, list_of_values))
    return len(list_filtered_result)


def divided_by_x(list_of_values: list, x: int):
    """
     wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
    :param list_of_values: lista wartości z których ma być wybrana
    :param x: wartość progowa
    :return: lktóre są podzielne przez `x`
    """
    list_filtered_result = list(filter(lambda y: True if y % x == 0 else False, list_of_values))
    return list_filtered_result


def first_divided_by_x(list_of_values: list, x: int):
    """
     - `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
    :param list_of_values: lista wartości z których ma być wybrana
    :param x: wartość progowa
    :return: pierwsza które jest podzielna przez `x`
    """
    list_filtered_result = list(filter(lambda y: True if y % x == 0 else False, list_of_values))
    if len(list_filtered_result) == 0:
        return None
    else:
        return list_filtered_result[0]


def find_common(lista1: list, lista2: list):
    """
    - `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma nie.
    :param liasta1: pierwsza lista liczb
    :param lista2: druga lista liczb
    :return:
    """
    common = [i for i in lista1 if i in lista2]
    if len(common) == 0:
        return None
    else:
        return common


# lista_ =[1,2,0,3,4,6]
# lista_1 =[4,6,1]
# print (f" {suma(lista_)}")
# print (f" {srednia(lista_)}")
# # print (f" {max_(lista_)}")
# # print (f" {diff_max_min(lista_)}")
# # print (f" {diff_max_min(lista_)}")
# print (f" {print_bigger(lista_, 2)}")
# print (f" {first_bigger(lista_, 2)}")
# print (f" {first_bigger([1,-1,-4,0], 2)}")
# print (f" {sum_bigger(lista_, 2)}")
# print (f" {no_of_bigger(lista_, 2)}")
# print (f" {divided_by_x(lista_, 2)}")
# print (f" {first_divided_by_3(lista_, 2)}")
# print (f" {find_common(lista_,lista_1)}")


def test_suma_multi_value():
    tests = [([1, 2, 3, 4], 10), ([-1, 0, 1], 0), ([-5.3, -19.5, 22.1], -2.7)]
    for n, wynik in tests:
        assert suma(n) == wynik

def test_srednia_multi_value():
    tests = [([1, 2, 3, 4], 2.5), ([-1, 0, 1], 0), ([-5.3, -19.5, 22.1], -0.9)]
    for n, wynik in tests:
        assert srednia(n) == wynik

def test_max_multi_value():
    tests = [([1, 2, 3, 4], 4), ([-1, 0, 1], 1), ([-5.3, -19.5, 22.1], 22.1)]
    for n, wynik in tests:
        assert max_(n) == wynik

def test_diff_max_min_multi_value():
    tests = [([1, 2, 3, 4] ,3), ([-1, 0, 1], 2), ([-5.3, -19.5, 22.1], 41.6)]
    for n, wynik in tests:
        assert diff_max_min(n) == wynik

def test_print_bigger_multi_value():
    tests = [([1, 2, 3, 4], 2 ,[3, 4]), ([-1, 0, 1], -0.1 ,[0, 1]), ([-5.3, -19.5, 22.1], -6.1 ,[-5.3,  22.1])]
    for n,m, wynik in tests:
        assert print_bigger(n,m) == wynik

def test_first_bigger_multi_value():
    tests = [([1, 2, 3, 4], 2 ,3), ([-1, 0, 1], -0.1 ,0), ([-5.3, -19.5, 22.1], -6.1 ,-5.3), ([-5.3, -19.5, 22.1], 33 ,None)]
    for n,m, wynik in tests:
        assert first_bigger(n,m) == wynik

def test_sum_bigger_multi_value():
    tests = [([1, 2, 3, 4], 2 ,7), ([-1, 0, 1], -0.1 ,1), ([-5.3, -19.5, 22.1], -6.1 ,16.8), ([-5.3, -19.5, 22.1], 33 ,0)]
    for n,m, wynik in tests:
        assert sum_bigger(n,m) == wynik

def test_sum_bigger_multi_valueError():
    with pytest.raises(ValueError):
        tests = [ ([-5.3, -19.5, 22.1], 33 ,0)]
        for n,m, wynik in tests:
         assert sum_bigger(n,m) == wynik

def test_no_of_bigger_multi_value():
    tests = [([1, 2, 3, 4], 2 ,2), ([-1, 0, 1], -0.1 ,2), ([-5.3, -19.5, 22.1], -6.1 ,2),  ([-5.3, -19.5, 22.1], 33 , 0)]
    for n,m, wynik in tests:
        assert no_of_bigger(n,m) == wynik

def test_divided_by_x_multi_value():
    tests = [([1, 2, 3, 4], 2 ,[2, 4] ), ([-1, 0, 1], -0.1 ,[0]), ([-5.3, -19.5, 22.1], -6.1 ,[]),  ([-5.3, -19.5, 22.1], 33 , [])]
    for n,m, wynik in tests:
        assert divided_by_x(n,m) == wynik

def test_first_divided_by_x_multi_value():
    tests = [([1, 2, 3, 4], 2 , 2), ([-1, 0, 1], -0.1 ,0), ([-5.3, -19.5, 22.1], -6.1 ,None),  ([-5.3, -19.5, 22.1], 33 , None)]
    for n,m, wynik in tests:
        assert first_divided_by_x(n,m) == wynik


def test_find_common_multi_value():
    tests = [([1, 2, 3, 4], [2,-1,-4] , [2]), ([-1, 0, 1], [1,1,0] ,[0,1]), ([-5.3, -19.5, 22.1], [-19.3] ,None),  ([-5.3, -19.5, 22.1], [] , None)]
    for n,m, wynik in tests:
        assert find_common(n,m) == wynik