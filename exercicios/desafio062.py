"""
Desafio 062 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser que quer
mostrar 0 termos.
"""

termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
cont = 1
qtd = 10  # quantidade inicial
adicional = -99  # termos adicionais
while adicional != 0:
    while cont <= qtd:
        print(f'{cont}° termo: {termo}')
        termo += razao
        cont += 1
    adicional = int(input('Quantos termos quer mostrar a mais? Digite o valor '
                          'desejado\nou digite 0 para finalizar o programa: '))
    # caso preenchimento vazio ou número negativo:
    if adicional < 0:
        adicional = int(input('Informe um número válido: '))
    qtd += adicional
print('Programa encerrado com sucesso!')
