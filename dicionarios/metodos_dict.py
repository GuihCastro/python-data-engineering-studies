contacts = {
    "Gui": {"name": "Guilherme", "phone": "91234-5678"},
    "Mari": {"name": "Mariana", "phone": "98765-4321"},
    "Mag": {"name": "Maggie", "phone": "93456-7890"},
    "Lasanha": {"name": "Kurt", "phone": "90987-6432", "feature": {"bochechas": "GG"}},
}

# copy
contacts_copy = contacts.copy()
print(contacts_copy)

# clear
contacts_copy.clear()
print(contacts_copy)

# fromkeys
contacts_new = dict.fromkeys(["name", "phone"])
print(contacts_new)
contacts_new = dict.fromkeys(["name", "phone"], "Campo vazio")
print(contacts_new)

# get
print(contacts.get("Guts", "Campo não encontrado"))
print(contacts.get("Gui", "Camoi não encontrado"))

# items
print(contacts.items()) # retorna uma lista de tuplas

# pop
print(contacts.pop("Gui"))
print(contacts)

# popitem
print(contacts.popitem())
print(contacts)

# setdefault
contacts.setdefault("Mari", {"age": 32})
print(contacts)
contacts.setdefault("Gui", {"name": "Guilherme", "age": 32})
print(contacts)

# update
contacts.update({"Mari": {"name": "Mariana", "age": 32}})
contacts.update({"Mag": {"name": "Maggie", "age": 8}})
contacts.update({"Lasanha": {"name": "Kurt", "age": 7}})
print(contacts)

# values
print(contacts.values())

# in
print("Gui" in contacts)
print("Red" in contacts)
print("age" in contacts["Lasanha"])
print("phone" in contacts["Mag"])

# del
del contacts["Lasanha"]["age"]
print(contacts)
del contacts["Gui"]
print(contacts)
del contacts
print(contacts)