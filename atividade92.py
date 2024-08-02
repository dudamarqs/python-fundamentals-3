from datetime import datetime

dados = dict()

dados['Nome'] = str( input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira'] = int(input('Carteira de Trabalho: '))

if dados['carteira'] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano de contratação'] + 35) - datetime.now().year)

print()
for k, v in dados.items():
    print(f'- {k} é igual a {v}')