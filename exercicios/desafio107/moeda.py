def aumentar(preco, taxa):
    a = preco * (taxa / 100)
    return preco + a


def diminuir(preco, taxa):
    d = preco * (taxa / 100)
    return preco - d


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco / 2
