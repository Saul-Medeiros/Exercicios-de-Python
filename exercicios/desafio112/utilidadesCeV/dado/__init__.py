def leiadinheiro(prompt):
    while True:
        # variável principal
        preco = str(input(prompt)).strip()
        # variável auxiliar que passará por teste numérico no lugar da variável
        # principal
        num = preco
        # se tiver vírgula ou pontuação no número
        if ',' in num:
            # variável auxiliar remove a vírgula
            num = preco.replace(',', '')
        if '.' in num:
            num = preco.replace('.', '')
        # se num não for numérico
        if not num.isnumeric():
            print(f'\033[31mERRO: \"{preco}\" é um preço inválido!\033[m')
        else:
            if ',' in preco:
                # troca a vírgula por ponto da variável principal para poder
                # ser feita a conversão para float
                preco = preco.replace(',', '.')
            # string convertida para float
            preco = float(preco)
            break
    return preco
