"""

Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).

Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie, m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy
"""

class Thing:
    def __init__(self, attribute):
        self._attr_name = attribute

    def __str__(self):
        return self._attr_name


class Subject(Thing):
    def __init__(self, attribute, subject_text):
        super().__init__(attribute)
        self._subject_text = subject_text

    def __str__(self):
        return f'{self._attr_name}:  {self._subject_text} \n' + "=" * len(self._attr_name) + '\n'


class Description(Thing):
    def __init__(self, attribute, description):
        super().__init__(attribute)
        self._description = description

    def __str__(self):
        return f'{self._attr_name}:\n' + "-" * len(self._attr_name) + f'\n{self._description}'

class Price(Thing):
    def __init__(self, attribute, price_value):
        super().__init__(attribute)
        self._price = price_value

    def __str__(self):
        return f'{self._attr_name}: {self._price}'

class SellerProfile(Thing):
    def __init__(self, attribute, first_name,last_name,phone,email):
        super().__init__(attribute)
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._email = email

    def __str__(self):
        return f'{self._attr_name}: \nUżytkownik: {self._first_name} {self._last_name}\ntel: \t\t{self._phone}\nemail: \t\t{self._email}'

class Announcement:
    def __init__(self):
        self._components = []

    def add_element(self, component: Thing):
        if not isinstance(component, Thing):
            raise TypeError('You can add only Things  to document.')

        self._components.append(component)

    def __str__(self):
        rendered_announcemen = []
        for component in self._components:
            rendered_announcemen.append(str(component))

        return '\n'.join(rendered_announcemen)

    def render(self):
        print(self.__str__())

announcement = Announcement()
announcement.add_element(Subject('Subject','Sprzedam Rower Górski'))
announcement.add_element(Description('Opis', '\t-Rower w stanie dobrym\n\t-Przerzutki do regulacji\n\t- posiada ślady użytkowania\n\t- nowe opony i siodełko\n\t-koła 26\n\t-wygodny'))
announcement.add_element(Price('Cena','375 PLN'))
announcement.add_element(SellerProfile('\nProfil','Teodor','Roosvelt','+48123456789','teodor.roosvelt@gmail.com'))
print(announcement)
