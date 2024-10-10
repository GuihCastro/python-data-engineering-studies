# sem argumentos
def show_message():
    print("Hello, World!")

# com argumento default (opcional)
def show_message_2(name="Usuário"):
    print(f"Olá, {name}! Seja bem-vindo(a)!")

# com argumento obrigatório
def show_message_3(name):
    print(f"Olá, {name}! Seja bem-vindo(a)!")

print("Função sem argumento:")
show_message()
print("Função com argumento default (opcional) sem passar o argumento:")
show_message_2()
print("Função com argumento default (opcional) passando o argumento:")
show_message_2("Guilherme")
print("Função com argumento obrigatório:")
show_message_3("Guilherme")
