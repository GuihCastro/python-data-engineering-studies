def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def show_result(a, b, func):
    result = func(a, b)
    print(f"O resultado da operação é: {result}")

show_result(10, 10, sum)
show_result(10, 10, subtract)