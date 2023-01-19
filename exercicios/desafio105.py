"""
Desafio 105 - Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguintes
informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
"""


def notas(*num, sit=False):
    """
    Função para analisar ntas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    total = len(num)
    media = 0
    maior = menor = num[0]
    for n in num:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        media += n
    media /= total
    boletim = {
        'total': total,
        'maior': maior,
        'menor': menor,
        'média': f'{media:.2f}'
    }
    if sit:
        if media < 7:
            boletim['situação'] = 'RUIM'
        else:
            boletim['situação'] = 'BOA'
    return boletim


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
