lista = []

# receber os valores pelo teclado
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))

# definir maior e menor
print(f'\nVocê digitou os valores {lista}.')
print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))}.')
