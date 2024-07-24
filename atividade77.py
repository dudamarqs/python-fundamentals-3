words = ('apartamento', 'computador', 'livro', 'telefone', 'jardim', 
         'avião', 'carro', 'cidade', 'amizade', 'futebol', 'escola', 
         'diamante', 'espada', 'basquete', 'caderno', 'livraria')

for word in words:
    print(f'\nNa palavra "{word}" temos: ', end='')
    for char in word:
        if char.lower() in 'aeiou':
            print(char, end=' ')
