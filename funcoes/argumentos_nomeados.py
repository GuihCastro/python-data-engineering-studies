def save_car(brand, model, year, plate):
    print(f"""
    Salvando carro no banco de dados...
    {brand}/{model}/{year}/{plate}
    """)

save_car("Honda", "Civic", 2024, "ABC-1234")
save_car(brand="Honda", model="Civic", year=2024, plate="ABC-1234")
save_car(**{"brand": "Honda", "model": "Civic", "year": 2024, "plate": "ABC-1234"})
