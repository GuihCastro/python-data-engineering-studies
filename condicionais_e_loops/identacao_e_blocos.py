def withdraw(value: float):
    balance = 500

    if balance >= value:
        balance -= value
        print("Valor sacado!")
        print(f"Saldo atual: {balance}")

value_to_withdraw = float(input("Informe o valor que deseja sacar: "))

withdraw(value_to_withdraw)