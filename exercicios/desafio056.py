"""
Desafio 056 - Desenvolva um programa que leia o nome, idade e sexo de
4 pessoas. No final do programa, mostre:
> A média da idade do grupo.
> Qual é o nome do homem mais velho.
> Quantas mulheres tem menos de 20 anos.
"""
nomeMaior = ''
idadeMaior = 0
mulheresMenor = 0
media = 0
for c in range(1, 5):
    print('-'*5, f'{c}ª PESSOA', '-'*5)
    # Remove espaços indesejados e deixa as primeiras letras de cada
    # frase em forma maiúscula:
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    # Remove espaços indesejados
    sexo = str(input('Sexo [M/F]: ')).strip()
    # Armazena a soma de todas as idades
    media += idade
    if sexo in 'Mm' or sexo in 'Ff':
        if sexo in 'Ff' and idade < 20:
            mulheresMenor += 1
        if sexo in 'Mm' and idadeMaior < idade:
            idadeMaior = idade
            nomeMaior = nome
    else:
        print('Informe um sexo válido e tente novamente.')
        exit()  # Finaliza o programa
# Após somar todas as idades, vai ser calculado a média de idade:
media /= 4
print('-'*21)
print(f'''{media} foi a média de idade entre as pessoas registradas.
{nomeMaior} é o nome do homem mais velho e o mesmo possui {idadeMaior} anos.
{mulheresMenor} mulheres tem menos de 20 anos.''')
