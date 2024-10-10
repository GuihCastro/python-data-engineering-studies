text = input("Digite um texto: ")
VOWELS = "AEIOU"
count = 0

# laço iterável
for letter in text:
    if letter.upper() in VOWELS:
        count += 1

if count > 1:
    print(f"Seu texto tem {count} vogais.")
elif count == 1:
    print("Seu texto tem apenas uma vogal.")
else:
    print("Seu texto não tem vogais.")

# função built-in range
for number in range(count):
    print(number, end=" ")
#for number in range(5, 50, 7):
#    print(number, end=" ")