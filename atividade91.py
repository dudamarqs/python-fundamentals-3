from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}

ranking = {}

print('Valores sorteados:')
sleep(1)

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

print('\n==== Ranking dos jogadores: ====')
sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
