cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

valor = int(input("Qual valor deseja sacar? R$"))
print("Você receberá:")

while valor != 0:

    if valor >= 100:
        while valor >= 100:
            valor = valor - 100
            cem = cem + 1
        print(f"{cem} notas de cem")

    if valor >= 50:
        while valor >= 50:
            valor = valor - 50
            cinquenta = cinquenta + 1
        print(f"{cinquenta} notas de cinquenta")

    if valor >= 20:
        while valor >= 20:
            valor = valor - 20
            vinte = vinte + 1
        print(f"{vinte} notas de vinte")

    if valor >= 10:
        while valor >= 10:
            valor = valor - 1
            dez = dez + 1
        print(f"{dez} notas de dez")

    if valor >= 5:
        while valor >= 5:
            valor = valor - 5
            cinco = cinco + 1
        print(f"{cinco} notas de cinco")

    if valor >= 2:
        while valor >= 2:
            valor = valor - 2
            dois = dois + 1
        print(f"{dois} notas de dois")

    if valor >= 1:
        while valor >= 1:
            valor = valor - 1
            um = um + 1
        print(f"{um} notas de um")
