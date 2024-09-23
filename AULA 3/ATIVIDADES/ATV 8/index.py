soma = 0

while True:
    numero = float(input("Digite sua nota (digite um número negativo para tirar a media das notas): "))
    if numero < 0:
        break
    elif numero > 0:
        soma += numero / numero
print("A media das suas notas é:", soma)