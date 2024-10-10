from abc import ABC, abstractproperty, abstractstaticmethod, abstractmethod


class RemoteControl(ABC):
    @property
    @abstractproperty
    def brand(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class TVControl(RemoteControl):
    @property
    def brand(self) -> str:
        return 'LG'

    def turn_on(self):
        print('Ligando a TV...')

    def turn_off(self):
        print('Desligando a TV...')


class MicroSystemControl(RemoteControl):
    @property
    def brand(self) -> str:
        return 'Sony'

    def turn_on(self):
        print('Ligando Micro System...')

    def turn_off(self):
        print('Desligando Micro System...')


control_1 = TVControl()
control_2 = MicroSystemControl()
print(control_1.brand, control_2.brand)
control_1.turn_on()
control_1.turn_off()
control_2.turn_on()
control_2.turn_off()