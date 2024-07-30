from random import randint

lista = list()
jogos = list()

print('-=' * 3, 'JOGO DA MEGA SENA', '-=' * 3)
num_jogos = int(input('Quantos jogos devo fazer? '))
total = 0

while total <= num_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print()
print('-=' * 3, f'SORTEANDO {num_jogos} JOGOS...', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
        