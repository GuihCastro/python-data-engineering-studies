while True:
    number = int(input("\nInforme um número inteiro: "))

    for n in range(number * 2):
        if n == number:
            continue
        print(n, end=" ")

    if number == 10:
        break