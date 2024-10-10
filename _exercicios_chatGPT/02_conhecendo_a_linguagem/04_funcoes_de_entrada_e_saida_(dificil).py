# Crie um pequeno sistema de cadastro que solicite informações do usuário (nome, idade, e-mail) e exiba uma confirmação formatada dessas informações. Use input() para entrada e print() para saída, explorando diferentes opções de formatação.

print("""
=================================
Vamos dar início ao seu cadastro!
=================================
""")

name = input("Por favor, informe o seu nome: ")
age = int(input("Agora, informe a sua idade: "))
email = input("Por fim, o seu e-mail: ")

print(f"""
===============================
Cadastro realizado com sucesso!
Usuário: {name}
Idade: {age}
E-mail: {email}
===============================
""")