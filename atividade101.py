def voto(ano):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos, o voto é negado.'
    elif 16 < idade < 65:
        return f'Com {idade} anos, o voto é obrigatório.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o voto é opcional.'

ano = int(input('Em que ano você nasceu? '))
print(voto(ano))