pessoa = dict()
soma = media = 0
pessoas = list()

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Por favor, digite M ou F para indicar seu sexo.')
    
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    
    while True:
        pergunta = input('Deseja continuar? [S/N] ').upper()[0]
        if pergunta in 'SN':
            break
        print('Digite apenas S ou N para indicar sua resposta.')
    if pergunta == 'N':
        break

print()
print(f'A) {len(pessoas)} pessoas foram cadastradas.')
media = soma / len(pessoas)
print(f'B) A média de idade entre os cadastrados é {media:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')

for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')

print()
print(f'D) Pessoas com idade acima da média: ', end='')
for p in pessoas:
    if p['idade'] > media:
        print(f'{p["nome"]} ', end='')
