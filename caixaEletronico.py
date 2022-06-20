cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

valor = int(input("Qual valor deseja sacar? R$"))

while valor != 0:

    if valor >= 100:
        while valor >= 100:
            valor = valor - 100
            cem = cem + 1

    if valor >= 50:
        while valor >= 50:
            valor = valor - 50
            cinquenta = cinquenta + 1

    if valor >= 20:
        while valor >= 20:
            valor = valor - 20
            vinte = vinte + 1

    if valor >= 10:
        while valor >= 10:
            valor = valor - 1
            dez = dez + 1

    if valor >= 5:
        while valor >= 5:
            valor = valor - 5
            cinco = cinco + 1

    if valor >= 2:
        while valor >= 2:
            valor = valor - 2
            dois = dois + 1

    if valor >= 1:
        while valor >= 1:
            valor = valor - 1
            um = um + 1

print(f"Você receberá:\n {cem} notas de R$100\n {cinquenta} notas de R$50\n {vinte} notas de R$20\n {dez} notas de "
      f"R$10\n {cinco} notas de R$5\n {dois} notas de R$2\n {um} notas de R$1")
