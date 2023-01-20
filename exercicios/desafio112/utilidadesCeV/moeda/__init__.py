def aumentar(n, pcent=0, formatar=False):
    """
    -> Função que aumenta o valor de acordo com o percentual informado, e
    possibilita formatação opcional do resultado.
    :param n: Valor a ser alterado.
    :param pcent: Porcentagem de aumento do valor.
    :param formatar: Opção para formatação, caso seja False ou não
    preenchido, vai retornar sem a formatação.
    :return: O valor aumentado de acordo com a porcentagem informada, com ou
    sem formatação.
    """
    a = n * (pcent / 100)
    if not formatar:
        return n + a
    else:
        return moeda(n + a)


def diminuir(n, pcent=0, formatar=False):
    """
        -> Função que diminui o valor de acordo com o percentual informado, e
        possibilita formatação opcional do resultado.
        :param n: Valor a ser alterado.
        :param pcent: Porcentagem de redução do valor.
        :param formatar: Opção para formatação, caso seja False ou não
        preenchido, vai retornar sem a formatação.
        :return: O valor reduzido de acordo com a porcentagem informada, com ou
        sem formatação.
        """
    d = n * (pcent / 100)
    # se formatar for falso
    if not formatar:
        return n - d
    # se formatar for verdadeiro
    else:
        return moeda(n - d)


def dobro(n, formatar=False):
    """
    -> Função que calcula o dobro do valor a ser informado, tendo como
    opcional a formatação.
    :param n: Valor a ser calculado
    :param formatar: Opção para formatação, caso seja False ou não
    preenchido, vai retornar sem a formatação.
    :return: O dobro do valor, com ou sem formatação
    """
    if not formatar:
        return n * 2
    else:
        return moeda(n * 2)


def metade(n, formatar=False):
    """
    -> Função que calcula a metade do valor a ser informado, tendo como
    opcional a formatação.
    :param n: Valor a ser calculado
    :param formatar: Opção para formatação, caso seja False ou não
    preenchido, vai retornar sem a formatação.
    :return: A metade do valor, com ou sem formatação
    """
    if not formatar:
        return n / 2
    else:
        return moeda(n / 2)


def moeda(n):
    """
    -> Função para formatação de moeda no padrão brasileiro.
    :param n: Valor a ser formatado.
    :return: Valor formatado.
    """
    reais = f'R${n:.2f}'
    return reais.replace('.', ',')


def resumo(n, aum=0, dim=0):
    """
    -> Função para criar um resumo do valor a ser analisado, contendo opcionais
    de aumento e redução, mostra também o dobro, ambos já com a formatação da
    moeda.
    :param n: Valor a ser analisado
    :param aum: Opcional de aumento
    :param dim: Opcional de redução
    :return: Resumo do valor com formatações
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    # \t = tabulação (tab)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{moeda(dobro(n))}')
    print(f'Metade do preço: \t{moeda(metade(n))}')
    print(f'{aum}% de aumento: \t{moeda(aumentar(n, aum))}')
    print(f'{dim}% de redução: \t{moeda(diminuir(n, dim))}')
    print('-' * 30)
