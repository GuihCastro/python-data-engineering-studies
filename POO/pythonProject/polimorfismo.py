class Bird:
    def fly(self):
        print(f'{self.__class__.__name__} voando...')


class Sparrow(Bird):
    def fly(self):
        super().fly()


class Ostrich(Bird):
    def fly(self):
        print(f'{self.__class__.__name__} não pode voar...')


# NOTE: exemplo ruim do uso de herança para "ganhar" um método
class Airplane(Bird):
    def fly(self):
        print(f'{self.__class__.__name__} decolando...')


def flight_plan(obj: object):
    obj.fly()


# main
sparrow = Sparrow()
ostrich = Ostrich()
airplane = Airplane()

flight_plan(sparrow)
flight_plan(ostrich)
flight_plan(airplane)
