numbers = []

while True:
    n = int(input('Digite um número (999 para finalizar): '))

    if n == 999:
        break

    numbers.append(n)

print(f'\nQuantidade de números digitados: {len(numbers)}.')
numbers.sort(reverse=True)
print(f'Números em ordem decrescente: {numbers}.')

if 5 in numbers:
    print('O número 5 aparece na lista.')
else:
    print('O número 5 não aparece na lista.')