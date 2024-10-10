contacts = {
    "Gui": {"name": "Guilherme", "phone": "91234-5678"},
    "Mari": {"name": "Mariana", "phone": "98765-4321"},
    "Mag": {"name": "Maggie", "phone": "93456-7890"},
    "Lasanha": {"name": "Kurt", "phone": "90987-6432", "feature": {"bochechas": "GG"}},
}

for key in contacts: # "errado"
    print(key, contacts[key])

for key, value in contacts.items(): # "correto"
    print(key, value)
