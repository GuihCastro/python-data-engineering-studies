from time import sleep


class Vehicle:
    def __init__(self, nbr_wheels: int, color: str, plate: str):
        self.nbr_wheels = nbr_wheels
        self.color = color
        self.plate = plate

    def turn_on(self):
        print(f'Ligando o motor de {self.__class__.__name__}', end='')
        sleep(.5)
        print('.', end='')
        sleep(.5)
        print('.', end='')
        sleep(.5)
        print('.')
        sleep(.5)
        print('Motor ligado!')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}'


class Bike(Vehicle):
    def dar_grau(self):
        print(f'Dando grau com {self.__class__.__name__}', end='')
        sleep(.5)
        print('.', end='')
        sleep(.5)
        print('.', end='')
        sleep(.5)
        print('.')
        sleep(.5)
        print('Grau dado!')


class Car(Vehicle):
    pass


class Truck(Vehicle):
    def __init__(self, nbr_wheels: int, color: str, plate: str, is_loaded: bool=False):
        super().__init__(nbr_wheels, color, plate)
        self.is_loaded = is_loaded

    def load_truck(self):
        print(f'Carregando {self.__class__.__name__}', end='')
        sleep(.5)
        print('.', end='')
        sleep(.5)
        print('.', end='')
        sleep(.5)
        print('.')
        sleep(.5)
        self.is_loaded = True
        print('Caminhão carregado!')


# Programa Principal
bike = Bike(2, 'amarela', 'abc-1234')
car = Car(4, 'preto', 'xyz-0666')
truck = Truck(6, 'branco', 'zzz-0000')

print(f'{bike}\n{car}\n{truck}')

car.turn_on()
bike.turn_on()
bike.dar_grau()
truck.load_truck()
truck.turn_on()

print(f'{bike}\n{car}\n{truck}')
