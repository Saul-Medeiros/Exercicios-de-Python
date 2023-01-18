"""
Desafio 083 - Crie um programa onde o usuário digite uma expressão qualquer que
use parênteses. Seu aplicativo deverá analisar se a expressão passada está com
os parênteses abertos e fechados na ordem correta.
"""
expression = str(input('Digite a expressão: '))
pilha = []
for simbolo in expression:  # recebe os caracteres da String
    if simbolo == '(':
        pilha.append('(')  # adiciona '(' a pilha
    elif simbolo == ')':
        # se tiver parênteses abertos pra fechar
        if len(pilha) > 0:
            pilha.pop()  # remove '('
        # se começar com ')' ou se não tiver nenhum '('
        else:
            pilha.append(')')  # acrescenta ')'
            break  # fim da repetição
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
