"""

Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).

Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie, m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy

Do zadania z klasą `Ogloszenie` dodaj kolejne klasy, które po niej dziedziczą.

`OgloszenieSamochodowe` – dziedziczy z `Ogloszenie` i dodatkowo określa cechy sprzedawanego samochodu jak model, markę, rok produkcji, przebieg, pojemność, moc i rodzaj paliwa.
`OgloszenieMieszkaniowe` – też dziedziczy z `Ogloszenie`, a dodatkowo cechy sprzedawanego mieszkania / domu: miejscowość, metraż, liczba pokoi.
"""


class Thing:
    def __init__(self, attribute: str):
        self._attr_name = attribute

    def __str__(self):
        return self._attr_name


class Subject(Thing):
    def __init__(self, attribute: str, subject_text: str):
        super().__init__(attribute)
        self._subject_text = subject_text

    def __str__(self):
        return f'{self._attr_name}:  {self._subject_text} \n' + "=" * len(self._attr_name) + '\n'


class Description(Thing):
    def __init__(self, attribute: str, description: str):
        super().__init__(attribute)
        self._description = description

    def __str__(self):
        return f'{self._attr_name}:\n' + "-" * len(self._attr_name) + f'\n{self._description}'


class Price(Thing):
    def __init__(self, attribute: str, price_value: int):
        super().__init__(attribute)
        self._price = price_value

    def __str__(self):
        return f'{self._attr_name}: {self._price}'


class SellerProfile(Thing):
    def __init__(self, attribute, first_name: str, last_name: str, phone: str, email: str):
        super().__init__(attribute)
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._email = email

    def __str__(self):
        return f'{self._attr_name}: \nUżytkownik: {self._first_name} {self._last_name}\ntel: \t\t{self._phone}\nemail: \t\t{self._email}'


class CarAttributes(Thing):
    def __init__(self, attribute, brand: str, model: str, year: int, course: int, power: float, displacement: float,
                 fuel_type: str):
        super().__init__(attribute)
        self._brand = brand
        self._model = model
        self._year = year
        self._course = course
        self._power = power
        self._displacement = displacement
        self._fuel_type = fuel_type

    def __str__(self):
        return f'{self._attr_name}: \nProducent: {self._brand} Model: {self._model}\nRocznik: \t\t{self._year}\nprzebieg: \t\t{self._course}\nMoc: \t\t\t{self._power} KM \nPojemność: \t\t{self._displacement} cm3 \nRodz. Paliwa: \t{self._fuel_type} '


class FlatAttributes(Thing):
    def __init__(self, attribute, city: str, area: float, rooms: int):
        super().__init__(attribute)
        self._city = city
        self._area = area
        self._rooms = rooms

    def __str__(self):
        return f'{self._attr_name}: \nMiasto: \t\t{self._city} \nPowierzchnia: \t{self._area}\nIlość pokoi: \t{self._rooms} '


class Announcement:
    def __init__(self):
        self.components = []

    def add_element(self, component: Thing):
        if not isinstance(component, Thing):
            raise TypeError('You can add only Things  to document.')

        self.components.append(component)

    def __str__(self):
        rendered_announcemen = []
        for component in self.components:
            rendered_announcemen.append(str(component))

        return '\n'.join(rendered_announcemen)

    def render(self):
        print(self.__str__())


class CarAnoncement(Announcement):
    def __init__(self):
        super().__init__()

    def add_car(self, component: Announcement):
        if not isinstance(component, Announcement):
            raise TypeError('You can add only Announcement  to document.')

        self.components.append(component)

    def __str__(self):
        rendered_announcemen = []
        for component in self.components:
            rendered_announcemen.append(str(component))

        return '\n'.join(rendered_announcemen)


class FlatAnoncement(Announcement):
    def __init__(self):
        super().__init__()

    def add_car(self, component: Announcement):
        if not isinstance(component, Announcement):
            raise TypeError('You can add only Announcement  to document.')

        self.components.append(component)

    def __str__(self):
        rendered_announcemen = []
        for component in self.components:
            rendered_announcemen.append(str(component))

        return '\n'.join(rendered_announcemen)


# ogłoszenie rowerowe
announcement = Announcement()
announcement.add_element(Subject('\nSubject', 'Sprzedam Rower Górski'))
announcement.add_element(Description('Opis',
                                     '\t-Rower w stanie dobrym\n\t-Przerzutki do regulacji\n\t- posiada ślady użytkowania\n\t- nowe opony i siodełko\n\t-koła 26\n\t-wygodny'))
announcement.add_element(Price('Cena', '375 PLN'))
announcement.add_element(SellerProfile('\nProfil', 'Teodor', 'Roosvelt', '+48123456789', 'teodor.roosvelt@gmail.com'))
print(announcement)

# ogłoszenie samochodowe
car_anoncement = Announcement()
car_anoncement.add_element(Subject('\nSubject', 'Sprzedam Toyota Avcensis'))
car_anoncement.add_element(CarAttributes('Dane Samochodu', 'Toyota', 'Avensis', 1999, 132000, 140, 1440, 'Benzyna'))
car_anoncement.add_element(Description('\nOpis',
                                       '\t- samochód w stanie dobrym\n\t- w 2014 remont silnika\n\t- posiada ślady użytkowania\n\t- nowe opony zimowe koła 16"\n\t- Serwisowany w ASO\n\t- bez wypadkowy'))
car_anoncement.add_element(Price('Cena', '6375 PLN'))
car_anoncement.add_element(SellerProfile('\nProfil', 'Teodor', 'Roosvelt', '+48123456789', 'teodor.roosvelt@gmail.com'))
print(car_anoncement)

# ogłoszenie mieszkaniowe
car_anoncement = Announcement()
car_anoncement.add_element(Subject('\nSubject', 'Sprzedam Mieszkanie'))
car_anoncement.add_element(FlatAttributes('Dane Mieszkania', 'Kraków', 70, 3))
car_anoncement.add_element(Description('\nOpis',
                                       '\t- mieszkanie świeżo po remoncie\n\t- jasne: od wschodu południa\n\t- zamkniete osiedle\n\t- dobrze skomunikowane z centrum'))
car_anoncement.add_element(Price('Cena', '436375 PLN'))
car_anoncement.add_element(SellerProfile('\nProfil', 'Teodor', 'Roosvelt', '+48123456789', 'teodor.roosvelt@gmail.com'))
print(car_anoncement)
