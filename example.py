class Car():
    def __init__(self, make, model):
        self.public_make = make #открытый атрибут
        self._protected_model = model #защищенный атрибут
        self.__private_year = 2022  #приватный атрибут

    def public_method(self):
        return f'Это открытый метод.  Машина: {self.public_make} - {self._protected_model}'

    def _protected_method(self):
        return "Это защищенный метод"

    def __private_method(self):
        return "Это приватный метод"


class Electro_car(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_details(self):
        details = f"{self.public_make} - {self._protected_model}, Батарея - {self.battery_size}"
        return details

tesla = Electro_car('Tesla', 'MX', 20000)
print(tesla.public_make)
print(tesla.public_method())

# Доступ к приватному атрибуту и методу напрямую невозможен, но Python позволяет обойти это
# ограничение (не рекомендуется)

print(tesla._Car__private_year)   #Доступ к приватному атрибуту через путь класса (name mandling).
# Нужно прописать одно нижнее подчеркивание - название класса и сразу двойное подчеркивание

