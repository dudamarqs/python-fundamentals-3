ficha = list()

while True: 
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])
    resp = (input('Deseja continuar? (S/N) '))
    if resp in 'Nn':
        break

print()
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for i, aluno in enumerate(ficha):
    print(f'{i + 1:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

print()
opcao = int(input('''[1] Ver as notas de um aluno específico
[2] Finalizar programa
Opção: '''))

if opcao == 1:
    while True:
        opc = int(input('Deseja ver as notas de qual aluno? (999 para finalizar) '))
        if opc == 999:
            print('\nFinalizando...')
            break
        if  1 <= opc <= len(ficha):
            print(f'Notas de {ficha[opc - 1][0]}: {ficha[opc - 1][1]}')
        else:
            print('Índice inválido.')
elif opcao == 2:
    print('\nSaindo do programa...')
else:
    print('Opção iválida. Tente novamente.')
