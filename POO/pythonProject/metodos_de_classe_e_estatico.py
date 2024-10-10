from datetime import datetime


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    @classmethod
    def create_from_birth(cls, name: str, birth: int) -> object:
        age: int = datetime.today().year - birth
        return cls(name, age)

    @staticmethod
    def is_of_age(age: int):
        return age >= 18


gui = Person.create_from_birth('Guilherme', 1992)
print(gui.name, gui.age)
print(Person.is_of_age(gui.age))