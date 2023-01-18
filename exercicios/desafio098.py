"""
Desafio 098 - Faça um programa que tenha uma função chamada contador(), que
receba três parâmetros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada. (o usuário digita)
"""
from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de ', end='')
    if passo < 0:
        # impressão do número negativo em sua forma positiva
        print(f'{passo * -1} em {passo * -1}')
        if inicio < fim:
            # conversão do passo para número positivo
            passo *= -1
    elif passo > 0:
        print(f'{passo} em {passo}')
        if inicio > fim:
            # conversão do passo para número negativo
            passo *= -1
    # se passo equivaler a 0, o mesmo passará a valer 1 positivo ou negativo,
    # dependendo do valor inicial e final
    else:
        print(f'1 em 1')
        if inicio > fim:
            passo -= 1  # passo -1
        else:
            passo += 1  # passo 1
    cont = inicio
    while True:
        print(cont, end=' ')
        sleep(0.5)
        # contador soma o passo antes da verificação
        cont += passo
        # verifica se o contador ultrapassou a meta
        if inicio < fim:
            if cont > fim:
                break
        elif inicio > fim:
            if cont < fim:
                break
        # Se início for igual ao fim, a repetição é interrompida
        else:
            break
    print('FIM!')


# De 1 até 10 de 1 em 1
contador(1, 10, 1)
# De 10 até 0 de 2 em 2
contador(10, 0, -2)
# Contagem Personalizada
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
num = (
    int(input('Inicio: ')),
    int(input('Fim:    ')),
    int(input('Passo:  '))
)
contador(num[0], num[1], num[2])
