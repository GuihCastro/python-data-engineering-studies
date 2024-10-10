saldo = 1000
saque = 200
limite = 100

# saque_possivel = saque <= saldo or saque <= saldo + limite
saque_possivel = (not saque > saldo) and (not saque > saldo + limite)

print(saque_possivel)