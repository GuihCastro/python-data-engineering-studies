conta_normal = True
conta_universitaria = False

saldo = 2000
saque = float(input("Informe o valor que deseja sacar: "))
cheque_especial = 500

if conta_normal:
    if saldo >= saque:
        saldo -= saque
        print("Saque realizado com sucesso!")
    elif saldo + cheque_especial >= saque:
        cheque_especial -= saldo - saque
        saldo = 0
        print("Saque realizado utilizando o limite de Cheque Especial.")
    else:
        print("Saldo insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        saldo -= saque
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente.")
else:
    print("O sistema não reconheceu o seu tipo de conta. Entre em contato com o seu gerente.")