class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print('*plim plim...*')

    def parar(self):
        print('*freando...*')
        print('Bicicleta parada!')

    def correr(self):
        print('*pedala, pedala, pedala...*')
        print('Correndo...')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


bike_1 = Bicicleta('Vermelha', 'BMX', '2024', 666, aro=20)
print(bike_1.cor, bike_1.modelo, bike_1.ano, bike_1.valor)
bike_1.correr()
bike_1.buzinar()
bike_1.parar()

bike_2 = Bicicleta('Verde', 'Mountain', '2022', 500)
print(bike_1)
print(bike_2)
