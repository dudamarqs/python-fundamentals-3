makeup = ('Base Líquida Hidratante', 89.90,
          'Corretivo em Bastão', 45.50,
          'Pó Compacto Translúcido', 59.90,
          'Paleta de Sombras Nude', 129.00,
          'Máscara de Cílios', 69.90,
          'Lápis de Olho Preto', 24.90,
          'Delineador Líquido Preto', 39.90,
          'Blush em Pó', 54.90,
          'Batom Matte Vermelho', 34.90,
          'Gloss Labial Transparente', 28.50,
          'Removedor de Maquiagem', 49.90,
          'Primer Facial', 79.90,
          'Iluminador em Pó', 64.90,
          'Lápis de Sobrancelha', 31.50,
          'Spray Fixador de Maquiagem', 59.90
)

print('=' * 45)
print(f'{"Listagem de preços":^45}')
print('=' * 45)

for position in range(0, len(makeup)):
    if position % 2 == 0:
        print(f'{makeup[position]:.<35}', end='') #coloca pontos alinhados à esquerda
    else:
        print(f'R$ {makeup[position]:>7.2f}')