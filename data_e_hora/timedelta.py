from datetime import  datetime, timedelta

car_type = input("Informe o tipo de carro: ").lower()

time_p = 30
time_m = 45
time_g = 60
current_time = datetime.now()

if car_type == "p":
    estimated_time = current_time + timedelta(minutes=time_p)
    print(f"O carro chegou às {current_time.strftime("%H:%M")} e ficará pronto às {estimated_time.strftime("%H:%M")}")
elif car_type == "m":
    estimated_time = current_time + timedelta(minutes=time_m)
    print(f"O carro chegou às {current_time.strftime("%H:%M")} e ficará pronto às {estimated_time.strftime("%H:%M")}")
elif car_type == "g":
    estimated_time = current_time + timedelta(minutes=time_g)
    print(f"O carro chegou às {current_time.strftime("%H:%M")} e ficará pronto às {estimated_time.strftime("%H:%M")}")
else:
    print("Por favor, informe um tipo de carro válido.")