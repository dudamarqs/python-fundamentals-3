brasileirao_2024 = (
     'Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'São Paulo', 'Bahia', 'Cruzeiro', 'CA Paranaense', 'Red Bull Bragantino', 'Atlético Mineiro', 'Vasco da Gama', 'EC Juventude', 'Internacional', 'Corinthians', 'Criciúma', 'Cuiabá Esporte Clube', 'EC Vitória', 'Grêmio', 'Fluminense', 'AC Goianense'
     )


print ('''Sobre o Brasileirão 2024, o que deseja conferir?
       [A] Os 5 primeiros colocados 
       [B] Os últimos 4 colocados na tabela 
       [C] Os times em ordem alfabética
       [D] Escolher um time e ver sua classificação
       [E] Ver classificação completa''')

opção = str(input('\nOpção: ')).upper()

if opção == 'A':
        print(f'\nOs 5 primeiros colocados: \n{brasileirao_2024[:5]}')

elif opção == 'B':
    print(f'Os últimos 4 colocados: \n{brasileirao_2024[-4:]}')

elif opção == 'C':
    times_ordem_alfabetica = sorted(brasileirao_2024)
    print('Os times em ordem alfabética:')
    for time in sorted(brasileirao_2024):
         print(time)

elif opção == 'D':
    time = input('Digite o nome do time: ').strip().title()
    if time in brasileirao_2024:
        classificacao = brasileirao_2024.index(time) + 1
        print(f'{time} está na {classificacao}ª posição.')
    else:
        print('Time não encontrado na tabela.')

elif opção == 'E':
    print('\nClassificação completa:\n')
    for i, time in enumerate(brasileirao_2024, start = 1):
         print(f'{i}ª posição: {time}')
