"""
Desafio 065 - Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior
e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
"""
r = 'S'
maior = menor = media = c = 0
while r == 'S':
    n = int(input('Digite um número: '))
    c += 1  # contador para a quantidade de números informados
    if c == 1:
        maior = menor = n  # o maior e o menor valor vai ser o mesmo
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    media += n  # soma os valores
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    # Resposta inválida:
    while r != 'S' and r != 'N':
        r = str(input('Digite uma resposta válida: ')).strip().upper()[0]
media /= c  # divide os vaalores pela quantidade
print(f'\n{media} foi a média entre os números informados. Dentre eles,'
      f'\n{maior} é o maior valor e {menor} é o menor valor em registro.')
