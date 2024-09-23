soma = 0

while True:
    numero = float(input("Digite um número (um número negativo para sair): "))
    if numero < 0:
        break
    if numero > 0:
        soma += numero
print("A soma dos números positivos é:", soma)