def leiaInt(mensagem):
    ok = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;33mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
