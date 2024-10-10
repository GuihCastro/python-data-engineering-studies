# filtro com for simples
numbers = [1, 30, 21, 2, 9, 65, 34]
even_1 = []

for number in numbers:
    if number % 2 == 0:
        even_1.append(number)

print(even_1)

# filtro com comprehension
even_2 = [number for number in numbers if number % 2 == 0]

print(even_2)

# modificando valores com for simples
square_1 = []

for number in numbers:
    square_1.append(number ** 2)

print(square_1)

# modificando valores com comprehension
square_2 = [number ** 2 for number in numbers]

print(square_2)