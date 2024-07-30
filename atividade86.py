
matriz = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]

#colocar os valores na matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha} x {coluna}]: '))

print()
print('Matriz:')
#formatar a matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]} ', end='')
    print()