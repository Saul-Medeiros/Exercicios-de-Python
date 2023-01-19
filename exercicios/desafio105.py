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
    boletim = {
        'total': len(num),
        'maior': max(num),
        'menor': min(num),
        'média': sum(num)/len(num)
    }
    if sit:
        # média igual ou acima de 7
        if boletim['média'] >= 7:
            boletim['situação'] = 'BOA'
        # média igual ou acima de 5
        elif boletim['média'] >= 5:
            boletim['situação'] = 'RAZOÁVEL'
        # média abaixo de 5
        else:
            boletim['situação'] = 'RUIM'
    return boletim


# programa principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
