"""

Napisz programy, w których tworzysz listę ogłoszeń samochodowych, a następnie wyszukujesz ogłoszenia na podstawie ich parametrów.

Na przykład ogłoszenia o cenach z określonego przedziału.

Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać wyszukane. Użyj poznanych kolekcji do trzymania ogłoszeń.
Możesz zastosować metodę `filter` do wyszukiwania odpowiednich ogłoszeń.
"""
from collections import defaultdict
from typing import List


class Car:
    _next_id = 1

    def __init__(self, brand: str, model: str, color: str, price: float, year: int, course: int):
        self.id = Car._next_id
        Car._next_id += 1
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.year = year
        self.course = course

    def print_info(self):
        print(self.get_info())  # w metodzie mam dostep do atrybutow i metod danego obiektu

    def get_info(self) -> str:
        return f'id: {self.id}, Marka "{self.brand}", Model "{self.model}", Color "{self.color}",Przebieg : {self.course}, Rocznik : {self.year}, Cena: {self.price:.2f} PLN, '

    def __str__(self):
        return f' nr oferty: {self.id}, Marka "{self.brand}", Model "{self.model}", Color "{self.color}",Przebieg : {self.course}, Rocznik : {self.year}, Cena: {self.price:.2f} PLN '


class Otomoto:
    def __init__(self):
        self._items = defaultdict(int)

    def add_car(self, car: Car, quantity: int = 1):
        #                 zmienna  typ -> sprawdzamy czy zmienna jest danego typu, jak nie to wyjatek
        if not isinstance(car, Car):
            raise ValueError('car has to be an instance of a Car class.')

        if quantity < 1:
            raise ValueError('quantity has to be a positive number.')

        self._items[car] += quantity  # mozna by liczyć ilości podobnych

    def price_selector(self, bottom_value: int, top_value: int):
        print(f'\nsamochody w canie pomiędzy {bottom_value}PLN  i {top_value}PLN')
        values_from_bottom = dict(filter(lambda x: x[0].price >= bottom_value, self._items.items()))
        values_filtered = dict(filter(lambda x: x[0].price <= top_value, values_from_bottom.items()))
        return values_filtered
        # for car in values_filtered:
        #     print(
        #         f'Marka: {car.brand}, Model {car.model}, Color {car.color}, Przebieg: {car.course}, Rocznik: {car.year}, Cena: {car.price: .2f} PLN ')

    def year_selector(self, bottom_value: int, top_value: int):
        print(f'\nsamochody z lat pomiędzy {bottom_value}   {top_value}')
        values_from_bottom = dict(filter(lambda x: x[0].year >= bottom_value, self._items.items()))
        values_filtered = dict(filter(lambda x: x[0].year <= top_value, values_from_bottom.items()))
        for car in values_filtered:
            print(
                f'Marka: {car.brand}, Model {car.model}, Color {car.color}, Przebieg: {car.course}, Rocznik: {car.year}, Cena: {car.price: .2f} PLN ')

    def color_selector(self, color: dict):
        print(f'\nsamochody w kolorach {color} ')
        values = dict(filter(lambda x: x[0].color in color, self._items.items()))
        return values
        # for car in values:
        #     print(
        #         f'Marka: {car.brand}, Model {car.model}, Color {car.color}, Przebieg: {car.course}, Rocznik: {car.year}, Cena: {car.price: .2f} PLN ')

    @classmethod
    def with_cars(cls, cars: List[Car]):
        tmp = cls()
        for car in cars:
            tmp.add_car(car, 1)
        return tmp

    def bulk_cars(self, cars: List[Car]):

        for car in cars:
            self.add_car(car, 1)

    def __str__(self):
        rendered_list = []
        for car in self._items:

            tmp=f'Marka: {car.brand}, Model {car.model}, Color {car.color}, Przebieg: {car.course}, Rocznik: {car.year}, Cena: {car.price: .2f} PLN '

            rendered_list.append(str(tmp))

        return '\n'.join(rendered_list)

car1 = Car('Citroen', 'C5', 'biały', 4200, 1994, 320000)
car2 = Car('Suzuki', 'gitara', 'czerwony', 3800, 1994, 320000)
car3 = Car('Trabant', 'limuzyna', 'zielony', 2300, 1964, 320000)

volx_cars = [
    Car('Volxvagen', 'Passat', 'biały', 1000, 1994, 320000),
    Car('Volxvagen', 'Passat', 'biały', 2000, 1994, 320000),
    Car('Volxvagen', 'Passat', 'biały', 3000, 1994, 320000),
]

toyota_cars = [
    Car('Toyota', 'Corola', 'biały', 1000, 1989, 320000),
    Car('Toyota', 'Camry', 'biały', 2000, 1994, 320000),
    Car('Toyota', 'Avalon', 'biały', 3000, 1987, 320000),
]

otomoto = Otomoto.with_cars(volx_cars)
otomoto.bulk_cars(toyota_cars)
otomoto.add_car(car1, 1)
otomoto.add_car(car2, 1)
otomoto.add_car(car3, 1)

om_price=Otomoto.with_cars(otomoto.price_selector(2000, 4800))
print(om_price)


om_price=Otomoto.with_cars(otomoto.price_selector(2000, 4800))
om_price_color=Otomoto.with_cars(om_price.color_selector({'biały', 'zielony'}))

print(om_price_color)

#otomoto.year_selector(1970, 1990)
