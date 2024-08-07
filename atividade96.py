def area(largura, comprimento):
    area = largura * comprimento
    print(f'\nA área de um terreno {largura}x{comprimento} é {area}m².')
    

print('CONTROLE DE TERRENOS')
print('-' * 20)

lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))

area(lar, com)
