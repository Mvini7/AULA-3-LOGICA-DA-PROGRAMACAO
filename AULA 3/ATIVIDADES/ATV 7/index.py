mult = 0
numero = int(input("Digite um numero qualquer: "))

while mult < 10:
    mult += 1
    multiplicacao = numero * mult
    if multiplicacao % 3 == 0:
        print(f"{numero} x {mult} = {multiplicacao}")