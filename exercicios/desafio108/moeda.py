def aumentar(n, pcent=0):
    a = n * (pcent / 100)
    return n + a


def diminuir(n, pcent=0):
    d = n * (pcent / 100)
    return n - d


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(n):
    reais = f'R${n:.2f}'
    return reais.replace('.', ',')
