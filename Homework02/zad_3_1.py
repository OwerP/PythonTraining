"""
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr) podpowiedź: wartość PI jest dostępna jako `Math.PI`
5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

"""

import math
import pytest
def feet2meter(val_feet: float) -> float:
    """
    `feet2meter - stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
    :param val_feet: wartość wyrażona w stopach
    :return: wartość przeliczona za stóp na metry
    """
    value_meter = round(val_feet / 3.2808, 4)
    return value_meter


def max_(val1: float, val2: float)->float:
    """
    `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
    :param val1: pierwsza liczba
    :param val2: druga liczba
    :return: max z dwóch powyższych
    """
    if val1 > val2:
        return val1
    else:
        return val2

def avg_(val1: float, val2: float) -> float:
    """
    `srednia` - oblicza średnią z dwóch liczb,
    :param val1: pierwsza liczba
    :param val2: druga liczba
    :return: avg z dwóch powyższych
    """
    avg_val=(val1+val2)/2
    return avg_val

def circle_field(r: float)-> float:
    """
    `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr) podpowiedź: wartość PI jest dostępna jako `Math.PI`
    :param r: promień
    :return: pole koła o promieniu r
    """
    circ_f = round(math.pi * r**2,2)
    return circ_f

def bmi (masa: float, wzrost: float)-> float:
    """
    `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
    :param masa: masa człowieka [kg]
    :param wzrost: wzrost człowieka [m]
    :return: wartość współczynika BMI dla człowieka
    """
    if wzrost > 0 and masa > 0:
        wspolczynik=round(masa/wzrost**2,2)
        return wspolczynik
    else:
        raise ValueError("wzrost i masa musi być > 0")


def triangle_field(a: float, b: float, c: float)-> float:
    """
    `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
    :param a: miara pierwszego boku
    :param b: miara drugiego boku
    :param c: miara trzeciego boku
    :return: pole trójkata o bokach a,b,c
    """
    if a + b > c and b + c > a and a + c > b:
        p = (a + b + c) / 2
        field = round(math.sqrt(p * (p - a) * (p - b) * (p - c)),4)
        return field

def miles_vs_km(value: float, flag='m2k')->float:
    """
    7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
    8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry
    :param value: wartość metryki do przeliczeń
    :param flag: m2k lub k2m
    :return:
    """
    miles2km=0
    km2miles=0
    if flag == 'm2k':
        miles2km=round(value/0.62137,4)
        return miles2km
    elif flag =='k2m':
        km2miles=round(value*0.62137,4)
        return km2miles
    else:
        raise ValueError("flag has to be m2k or k2m")


def test_feet2meter_multi_value():

    tests = [(0, 0), (2.3, 0.7010), (10, 3.0480), (123.123, 37.5283)]
    for n, wynik in tests:
        assert feet2meter(n) == wynik

def test_max_multi_value():

    tests = [(0,0,0), (1.2,2.3, 2.3), (10,-1, 10), (-13.7,-17.1, -13.7)]
    for val1, val2, wynik in tests:
        assert max_(val1,val2) == wynik

def test_avg_multi_value():

    tests = [(0,0,0), (-1, 1, 0), (1.23,-3.276, -1.023), (-13.7,-17.1, -15.4)]
    for val1, val2, wynik in tests:
        assert avg_(val1,val2) == wynik

def test_circle_multi_value():

    tests = [(0,0), ( 1, 3.14), (3, 28.27), (13.7, 589.65)]
    for val1,  wynik in tests:
        assert circle_field(val1) == wynik

def test_bmi_multi_value():

    tests = [(68,1.65,24.98), (89, 1.72, 30.08), (95,1.72, 32.11), (103,1.72, 34.82)]
    for val1, val2, wynik in tests:
        assert bmi(val1,val2) == wynik

def test_triangle_field_multi_value():

    tests = [(2,2,3,1.9843), ( 1, 3.3,2.7, 1.1832), (0.71,1.23,0.99, 0.3514), (10.3,1.72,11, 8.3389)]
    for val1, val2, val3, wynik in tests:
        assert triangle_field(val1,val2, val3) == wynik

def test_miles_km_multi_value():

    tests = [(0,"m2k",0), (1, "k2m", 0.6214), (1,"m2k", 1.6093), (123,"k2m", 76.4285)]
    for val1, val2, wynik in tests:
        assert miles_vs_km(val1,val2) == wynik

