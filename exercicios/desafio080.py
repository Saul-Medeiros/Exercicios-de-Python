"""
Desafio 080 - Crie um programa onde o usuário possa digitar cinco valores
numéricos e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""
lista = []
for cont in range(1, 6):
    num = int(input(f'Digite o {cont}º número: '))
    # se contador igual a 1 ou o número for maior que o último item da lista
    if cont == 1 or num > lista[-1]:
        lista.append(num)
        print(f'O número {num} foi adicionado ao final da lista.')
    # se o num for menor que os últimos da lista
    else:
        # repetição de comparação do num com todos os itens da lista
        for n in range(0, len(lista)):
            if num < lista[n]:
                # insere o num na posição em que o item em comparação estava,
                # fazendo-o passar para a casa seguinte da lista
                lista.insert(n, num)
                print(f'O número {num} foi adicionado na posição {n}' if n > 0
                      else 'O número foi adicionado no início da lista.')
                break  # para a repetição atual
            # se o num for menor que o item da comparação atual
print(f'Lista Ordenada: {lista}')
