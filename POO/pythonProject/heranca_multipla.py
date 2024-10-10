class Animal:
    def __init__(self, paws: int):
        self.paws = paws

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}'


class Mammal(Animal):
    def __init__(self, fur: str, **kw):
        self.fur = fur
        super().__init__(**kw)


class Bird(Animal):
    def __init__(self, beak: str, can_fly: bool, **kw):
        self.beak = beak
        self.can_fly = can_fly
        super().__init__(**kw)


class Cat(Mammal):
    pass


class Platypus(Mammal, Bird):
    pass


cat = Cat(paws=4, fur='Laranja')
platypus = Platypus(paws=4, fur='Marrom', beak='Amarelo', can_fly=False)

print(f'{cat}\n{platypus}')
