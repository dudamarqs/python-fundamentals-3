c = ('\033[m',          # 0 - sem cor
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;33m'       # 6 - branco
    );

def ajuda(com):
    from time import sleep
    print(f'\n{c[4]}Acessando o manual do comando < {com} >...{c[0]}')
    sleep(1)

    help(com)


def titulo(mensagem, cor=0):
    tam = len(mensagem) + 4
    print(f'{c[cor]}=' * tam + f'{c[0]}')
    print(f'{c[cor]}  {mensagem}  {c[0]}')
    print(f'{c[cor]}=' * tam + f'{c[0]}')


comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 5)
    comando = str(input('Função ou Bibliteca (digite "fim" para finalizar) > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!', 2)
