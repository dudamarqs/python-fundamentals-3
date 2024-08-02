jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))

for c in range(0, total):
    partidas.append(int(input(f'    Quantos gols o jogador {jogador["nome"]} fez na partida {c+1}? ')))
jogador['nº de gols'] = partidas[:]
jogador['total de partidas'] = sum(partidas)

print('=' * 50)
for k, v in jogador.items():
    print(f'O campo {k} é igual a {v}.')

print('=' * 50)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["nº de gols"])} partidas:')

for i, v in enumerate(partidas):
    print(f'Na partida {i} fez {v} gols.')
print(f'\nAo todo, {jogador["nome"]} fez {jogador["total de partidas"]} gols.')