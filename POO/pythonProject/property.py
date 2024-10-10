from datetime import datetime


class Person:
    def __init__(self, name: str, birth: int):
        self.name: str = name
        self._birth: int = birth

    @property
    def age(self):
        age: int = datetime.today().year - self._birth
        return age


guilherme = Person('Guilherme', 1992)
print(f'Nome: {guilherme.name}, idade: {guilherme.age}')
