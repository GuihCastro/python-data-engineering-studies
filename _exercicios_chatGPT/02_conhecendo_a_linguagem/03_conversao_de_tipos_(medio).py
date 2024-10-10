# Crie um programa que solicite ao usuário dois números (como strings), converta-os para inteiros, e exiba a soma dos números. Inclua manipulação de erros caso o usuário insira valores não numéricos.

first_number = int(input("Informe o primeiro número para a soma: "))
second_number = int(input("Informe o segundo número para a soma: "))

result = first_number + second_number

print(f"A soma dos números informados é {result}")