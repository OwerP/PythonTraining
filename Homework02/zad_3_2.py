"""
Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.

Logikę obliczania liczby dni wydziel do osobnej funkcji.

**Wersja A**
Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.

**Wersja B (trudniejsza)**
Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.

"""

def lap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29
    else:
        return 28

def days_in_month(month: str):
    days31 = {'styczen', 'marzec', 'maj', 'lipiec', 'sierpien', 'pazdziernik', 'grudzien'}
    days30 = {'kwiecien', 'czerwiec', 'wrzesien', 'listopad'}
    month = month.lower()
    try:
        if month == 'luty':
            year = int(input('Podaj rok: '))
            return lap_year(year)
        elif month in days30:
            return 30
        elif month in days31:
            return 31
        else:
            raise ValueError
    except ValueError:
        print('Nie ma takiego miesiaca')
        exit()

identify_month=input("podaj nazwę miesiąca:")
days=days_in_month(identify_month)
print(f"miesiąc {identify_month} ma {days} dni")