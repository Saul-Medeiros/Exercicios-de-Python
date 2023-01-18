"""
Desafio 086 - Crie umm programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado.
0 □ □ □
1 □ □ □
2 □ □ □
  0 1 2
No final, mostre a matriz na tela com a formatação correta.
"""
matriz = []
# receber dados
for linha in range(0, 3):
    matriz.append(list())  # adiciona uma lista para cada linha
    for coluna in range(0, 3):
        matriz[linha].append(int(input('Digite um valor para a posição'
                                       f' [{linha}, {coluna}]: ')))
print('-=' * 30)
# mostrar dados
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
