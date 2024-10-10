# if | elif | else
def check_age(age: int):
    # if
    if age >= 18:
        return "Título de Eleitor OBRIGATÓRIO."
    # elif
    elif age < 18 and age >= 16:
        return "Título de Eleitor OPCIONAL."
    # else
    else:
        return "Ainda não pode tirar Título de Eleitor."

age = int(input("Informe a sua idade: "))

print(check_age(age))