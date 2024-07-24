numbers = []

while True:
    number = int(input('Digite um número (0 para finalizar): '))

    if number == 0:
        break

    if number not in numbers:
        numbers.append(number)
    else:
        print(f'{number} já foi digitado e não será inserido na lista.')

print(f'\nOs números digitados foram {numbers}.')

numbers.sort()
print(f'Os númeos digitados em ordem crescente: {numbers}.')