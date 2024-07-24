numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número de 0 a 20: '))
while not 0 <= num <= 20:
    print('Você escolheu um número fora do intervalo permitido, tente novamente')
    num = int(input('Digite um número de 0 a 20: '))

print(f'O número {num} escrito por extenso é "{numeros_extenso[num]}".')
