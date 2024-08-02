aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input('Média do aluno: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'

for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')
