dados = list()
temp = list()
maior_peso = menor_peso = 0

while True:
    temp.append(str(input('\nNome: ')))
    temp.append(float(input('Peso: ')))

    if len(dados) == 0:
        maior_peso = menor_peso = temp[1]
    else:
        if temp[1] > maior_peso:
            maior_peso = temp[1]
        if temp[1] < menor_peso:
            menor_peso = temp[1]

    dados.append(temp[:])

    pergunta = str(input('Deseja continuar? (S/N) '))
    if pergunta in 'Nn':
        break

    temp.clear()

print('=' * 30)
for c in dados:
    print(f'{c[0]} pesa {c[1]}kg.')

print(f'\nNúmero de pessoas caastradas: {len(dados)}.')
print(f'Pessoa(s) com o maior peso ({maior_peso}kg): ', end='')
for pessoa in dados:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]} ', end='')
print()

print(f'Pessoa(s) com o menor peso ({menor_peso}kg): ', end='')
for pessoa in dados:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]} ')
print()
