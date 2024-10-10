# Escreva um programa que calcule a área de um triângulo, armazenando os valores da base e altura em variáveis. Experimente usar constantes para valores fixos, como a proporção de 1/2 na fórmula da área.

base = float(input("Informe a base do triângulo: "))
height = float(input("Informe a altura do triângulo: "))
FORMULA = (base * height) / 2

print(f"A área do triângulo é: {FORMULA}")