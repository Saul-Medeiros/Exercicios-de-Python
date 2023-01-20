def aumentar(n, taxa=0, formatar=False):
    a = n * (taxa / 100)
    return n + a if formatar is False else moeda(n + a)


def diminuir(n, taxa=0, formatar=False):
    d = n * (taxa / 100)
    # se formatar for False
    if not formatar:
        return n - d
    # se formatar for True
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


def moeda(n):
    reais = f'R${n:.2f}'
    return reais.replace('.', ',')
