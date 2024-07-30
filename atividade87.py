matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
soma_pares = soma_coluna3 = maior_linha2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l} x {c}]: '))

print()
print('Matriz:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]} ', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()

for l in range(0, 3):
    soma_coluna3 += matriz[l][2]

for c in range(0, 3):
    if c == 0:
        maior_linha2 = matriz[1][c]
    elif matriz[1][c] > maior_linha2:
        maior_linha2 = matriz[1][c]

print()
print(f'Soma dos valores pares da matriz: {soma_pares}.')
print(f'Soma dos valores da 3ª coluna: {soma_coluna3}.')
print(f'Maior valor da 2ª linha: {maior_linha2}.')
