class Car:
    def __init__(self, brand, model, color, engine_on=False):
        print('Criando novo carro...')
        self.brand = brand
        self.model = model
        self.color = color
        print(f'{self.brand} {self.model} criado!')

    def turn_on(self):
        print('Dando partida...')
        self.engine_on = True
        print('*vrrruuummm...*')
        print('Carro ligado!')

    def turn_off(self):
        print('Desligando o carro...')
        self.engine_on = False
        print('Carro desligado!')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

    def __del__(self):
        print(f'Destruindo {self.brand} {self.model}...')
        print('*BOOM!!!*')


def create_new_car(brand, model, color):
    car = Car(brand, model, color)
    return car


car = create_new_car('Honda', 'Civic', 'Preto')
car_2 = create_new_car('Toyota', 'Corolla', 'Branco')
print(f'Seu novo carro: {car}')
car.turn_on()
print(f'Andando de {car.brand} {car.model}...')
print(f'Andando de {car.brand} {car.model}...')
print(f'Andando de {car.brand} {car.model}...')
del car_2
print(f'Andando de {car.brand} {car.model}...')
print(f'Andando de {car.brand} {car.model}...')
