num = (int(input('Digite o 1º número: ')),
           int(input('Digite o 2º número: ')),
           int(input('Digite o 3º número: ')),
           int(input('Digite o 4º número: '))
)

# mostrar em que posição o número 9 apareceu
if 9 in num:
    quant_nine = num.count(9) 
    times = 'vez' if quant_nine == 1 else 'vezes'
    print(f'\nO número 9 apareceu {num.count(9)} {times}.')
else:
    print('\nO número 9 não foi digitado.')

# mostrar em qual posição o número 3 apareceu
if 3 in num:
    print(f'O número 3 apareceu pela primeira vez na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')

# mostrar quais valores são pares
print('Número(s) par(es): ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
