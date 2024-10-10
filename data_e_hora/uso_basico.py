from datetime import date, datetime, time

dia = date(1992, 8, 10)
hoje = date.today()
print(dia)
print(hoje)

dia_e_hora = datetime(1992, 8, 10, 16, 15, 30)
hoje = datetime.today()
print(dia_e_hora)
print(hoje)

hora = time(16, 15, 30)
print(hora)