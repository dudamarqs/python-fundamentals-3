from time import sleep

def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    sleep(0.3)
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado é {maior}.')


maior(5, 2, 8, 1, 0)
maior(3, -2, 0, 5, 7, 2, 1, 13)
maior(2, 3, 1, 5)
maior(8, 5)
maior()
