from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Numeros sorteados: ', end='')

for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')