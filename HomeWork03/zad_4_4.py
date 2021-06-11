"""
Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody` (z początkową wartością 0).

Niech ta klasa ma metody `dolej` i `odlej`. Obie metody niech przyjmują argument `ile` i niech odpowiednio dodają lub odejmują tę liczbę do atrybutu `ilosc_wody`. Niech nie da się odlać więcej wody, niż jest w zbiorniku.

Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis `zbiornik z (ileś tam) litrami wody`.

Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`. Metoda dolej oprócz argumentu `ile` powinna też przyjmować argument `temperatura` oznaczający temperaturę dolewanej wody.
Dolanie wody do zbiornika powinno powodować zmianę temperatury wody w zbiorniku (zgodnie ze zwykłymi prawami fizyki).
"""


class Zbiornik:
    def __init__(self):
        self.ilosc_wody_w_zbiorniku = 0
        self.temperatura_wody_w_zbiorniku = 0

    def dolej(self, ilosc_wody: float, temperatura_wody: float):
        tmp_ilosc_wody_w_zbiorniku = self.ilosc_wody_w_zbiorniku
        self.ilosc_wody_w_zbiorniku += ilosc_wody
        self.temperatura_wody_w_zbiorniku = (tmp_ilosc_wody_w_zbiorniku * self.temperatura_wody_w_zbiorniku + ilosc_wody * temperatura_wody) / self.ilosc_wody_w_zbiorniku

    def odlej(self, ilosc_wody: float):
        if ilosc_wody <= self.ilosc_wody_w_zbiorniku:
            self.ilosc_wody_w_zbiorniku -= ilosc_wody
            return self.ilosc_wody_w_zbiorniku
        else:
            tmp = self.ilosc_wody_w_zbiorniku
            self.ilosc_wody_w_zbiorniku = 0
            return tmp

    def __str__(self):
        return (
            f'zbiornik z {self.ilosc_wody_w_zbiorniku} litrami wody o temperaturze {self.temperatura_wody_w_zbiorniku}')


zb = Zbiornik()
zb.dolej(300, 31)
print(zb)
zb.odlej(30)
print(zb)
zb.dolej(100, 1)
print(zb)
