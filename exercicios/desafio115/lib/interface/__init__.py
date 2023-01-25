def cores(cor=0):
    if cor == 1:
        return '\033[31m'  # Vermelho
    elif cor == 2:
        return '\033[32m'  # Verde
    elif cor == 3:
        return '\033[33m'  # Amarelo
    elif cor == 4:
        return '\033[34m'  # Azul
    else:
        return '\033[m'    # Tira a cor


def leiaint(prompt):
    while True:
        try:
            number = int(input(prompt))
        # caso valor informado não seja int
        except (ValueError, TypeError):
            print(f'{cores(1)}ERRO! Digite um número inteiro válido.{cores()}')
            continue
        else:
            return number


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(str(txt).center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cores(3)}{c}{cores()} - {cores(4)}{item}{cores()}')
        c += 1
    print(linha())
    opc = leiaint(f'{cores(2)}Sua Opção: {cores()}')
    return opc
