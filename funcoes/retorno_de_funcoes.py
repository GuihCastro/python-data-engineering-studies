# retorno explícito simples
def calculate_total(numbers):
    return sum(numbers)

# retorno explícito composto
def previous_and_next(number):
    previous = number - 1
    next = number + 1

    return previous, next

# retorno implícito (None) 
def message():
    print("Hello, World!")

print(calculate_total([10, 20, 30, 40]))
print(previous_and_next(666))
print(message())