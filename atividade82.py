numbers = []
odd_numbers = []
even_numbers = []

while True:
    n = int(input('Digite um número (999 para finalizar): '))

    if n == 999:
        break

    numbers.append(n)
    
    if n % 2 == 0:
        odd_numbers.append(n)
    else:
        even_numbers.append(n)

print(f'\nTodos os números: {numbers}.')
print(f'Números pares: {odd_numbers}.')
print(f'Números ímpares: {even_numbers}.')