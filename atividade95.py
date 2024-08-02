time = list()
jogador = dict()
partidas = list()
palavra_gol = 1

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, total):
        partidas.append(int(input(f'    Quantos gols o jogador {jogador["nome"]} fez na partida {c+1}? ')))
    jogador['nº de gols'] = partidas[:]
    jogador['total de partidas'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        pergunta = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if pergunta in 'SN':
            break
        print('Por favor, digite somente S ou N para indicar sua resposta.')
    if pergunta == 'N':
        break

print()
print('   Nº ', end='')
for i in jogador.keys():
    print(f'{i:<13}', end='')
print()

for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()


while True:
    busca = int(input('\nQuer ver informações de qual jogador? [999 para finalizar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'O jogador {busca} não foi cadastrado. Tente novamente...')
    else:
        print(f'=== INFORMAÇÕES DO JOGADOR {time[busca]["nome"]}: ===')
        print('=' * 50)
        print(f'O jogador {jogador["nome"]} jogou {len(jogador["nº de gols"])} partidas:')

        palavra_gol = 'gols' if jogador["total de partidas"] > 1 else 'gol'
        for i, v in enumerate(partidas):
            print(f'Na partida {i+1} fez {v} {palavra_gol}.')
        print(f'Ao todo, {jogador["nome"]} fez {jogador["total de partidas"]} {palavra_gol}.')