option = -1

while option != 0:
    option = int(input("[1] Sacar\n[2] Extrato\n[3] Depositar\n[0] Sair\nInforme a opção desejada: "))

    if option == 1:
        print("Sacando...")
    elif option == 2:
        print("Imprimindo Extrato...")
    elif option == 3:
        print("Depositando...")
    elif option == 0:
        print("Saindo...")
    else:
        print("Informe uma opção válida")

print("Encerrando o sistema...")