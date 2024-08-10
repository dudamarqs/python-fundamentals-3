def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número:
    parâmetro num: número que será calculado
    parâmetro show: (opcional) mostrar ou não a conta
    return: o valor do fatorial de um número
    """
    
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        fat *= c
    return fat

print(fatorial(5, show=True))
