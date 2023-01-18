"""
Desafio 049 - Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
"""
n = int(input('Informe um número: '))
print('\n++++ TABUADA DO NÚMERO {} ++++'.format(n))
for c in range(1, 11):
    print(f'{n} x {c:2} = {c * n}')
print('+'*29)
