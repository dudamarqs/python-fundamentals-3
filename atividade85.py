numeros = [[], []]
valor = 0

for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print(f'\nNumeros pares: {sorted(numeros[0])}.')
print(f'Números ímpares: {sorted(numeros[1])}.')