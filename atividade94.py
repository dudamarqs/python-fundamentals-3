pessoa = dict()
soma = media = 0
pessoas = list()

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
        if pessoa['sexo'] in 'MmFf':
            break
        print('Por favor, digite M ou F para indicar seu sexo.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        pergunta = input('Deseja continuar? [S/N] ')
        if pergunta in 'SsNn':
            break
        print('Digite apenas S ou N para indicar sua resposta.')
    if pergunta in 'Nn':
        break

print()
print(f'{len(pessoas)} foram cadastradas.')
media = soma / len(pessoas)
print(f'A média de idade entre os cadastrados é {media} anos.')
print('As mulheres cadastradas foram: ', end='')

for p in pessoas:
    if pessoa['sexo'] in 'Ff':
        print(f'{p['nome']} ', end='')
