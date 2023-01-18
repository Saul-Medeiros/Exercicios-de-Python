"""
Desafio 087 - Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
# matriz 3x3
matriz = []
somapares = maiorSL = somacoluna = 0
# inserção de valores no prompt
for linha in range(0, 3):
    matriz.append(list())  # adiciona uma lista para cada linha
    for coluna in range(0, 3):
        matriz[linha].append(int(input('Digite um valor para a posição'
                                       f' [{linha}, {coluna}]: ')))
        # números pares:
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
        # soma dos valores da 3ª coluna
        if coluna == 2:
            somacoluna += matriz[linha][2]
        # maior da segunda linha:
        if linha == 1:
            if coluna == 0:
                maiorSL = matriz[1][0]
            elif matriz[1][coluna] > maiorSL:
                maiorSL = matriz[1][coluna]
print('-=' * 30)

# impressão da matriz no prompt
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
print('-=' * 30)

print(f'''A soma dos valores pares é {somapares}.
A soma dos valores da terceira coluna é {somacoluna}.
O maior valor da segunda coluna é {maiorSL}.''')
