def aumentar(n, pcent=0, formatar=False):
    a = n * (pcent / 100)
    if not formatar:
        return n + a
    else:
        return moeda(n + a)


def diminuir(n, pcent=0, formatar=False):
    d = n * (pcent / 100)
    # se formatar for falso
    if not formatar:
        return n - d
    # se formatar for verdadeiro
    else:
        return moeda(n - d)


def dobro(n, formatar=False):
    if not formatar:
        return n * 2
    else:
        return moeda(n * 2)


def metade(n, formatar=False):
    if not formatar:
        return n / 2
    else:
        return moeda(n / 2)


def moeda(n=0):
    reais = f'R${n:.2f}'
    return reais.replace('.', ',')


def resumo(n=0, aum=0, dim=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    # \t = tabulação de texto (tab)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum}% de aumento: \t{aumentar(n, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(n, dim, True)}')
    print('-' * 30)
