"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
maiores = homens = mulhernova = 0
while True:
    print('-'*25 + f'\n{"FICHA CADASTRAL":^25}\n' + '-'*25)
    idade = int(input('Idade: '))
    resp = sexo = ' '  # redefine o valor de resp e de sexo a cada loop
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-'*25)
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulhernova += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\n{" FIM DO PROGRAMA ":=^43}\n' +
      f'''Total de pessoas com mais de 18 anos: {maiores}
Ao todo temos {homens} homens cadastrados
E temos {mulhernova} mulheres com menos de 20 anos.\n''' + '=' * 43)
