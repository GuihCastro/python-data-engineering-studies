class Account:
    def __init__(self, acc_number: str, balance: float=0):
        self.acc_number: str = acc_number
        self._balance: float = balance

    def deposit(self, value: float):
        self._balance += value
        print(f'Depósito no valor de R${value:.2f} realizado com sucesso!')

    def withdraw(self, value: float):
        self._balance -= value
        print(f'Saque no valor de R${value:.2f} realizado com sucesso!')

    def show_balance(self):
        print(f'Saldo atual: R${self._balance:.2f}')


# Programa principal
account = Account('0001')
print(account.acc_number)
account.deposit(10000)
account.withdraw(5000)
account.show_balance()
