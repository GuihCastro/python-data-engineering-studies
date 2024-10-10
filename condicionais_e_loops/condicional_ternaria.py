balance = 2000
withdraw = float(input("Informe o valor que deseja sacar: "))

status = "Sucesso" if withdraw <= balance else "Falha"

print(f"{status} ao realizar o saque.")