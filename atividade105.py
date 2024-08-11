def notas(*n, sit=False):
    """
    -> Função para analisar notas de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a turma.
    """
    relatorio = dict()
    relatorio['Total:'] = len(n)
    relatorio['Maior:'] = max(n)
    relatorio['Menor:'] = min(n)
    relatorio['Média:'] = sum(n)/len(n)
    
    if sit:
        if relatorio['Média'] >= 7:
            relatorio['Média'] = 'Boa'
        elif relatorio['Média'] >= 5:
            relatorio['Média'] = 'Razoável'
        else:
            relatorio['Média'] = 'Ruim'

    return relatorio


notas_alunos = list()

while True:
    nota = float(input('Digite a nota (000 para finalizar): '))
    if nota == 00:
        break

    notas_alunos.append(nota)

incluir_situação = input('Deseja incluir a situação? [s/n] ').strip().lower()
sit = incluir_situação == 's'

print(notas(*notas_alunos, sit))
