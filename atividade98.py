from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:') 
    sleep(1) 

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}, ', end='', flush=True)
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}, ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()

print('Sua vez de criar uma contagem personalizada!')
inicio = int(input('INÍCIO: '))
fim = int(input('FIM:    '))
passo = int(input('PASSO:  '))

print('\nContagem personalizada:')
contador(inicio, fim, passo)

