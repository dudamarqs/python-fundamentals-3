def ficha(jog='<desconhecido>', gols=0):
    print(f'\nO jogador {jog} fez {gols} gol(s).')


nome = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if nome.strip() == '':
    ficha(gols=g)
else:
    ficha(nome, g)
