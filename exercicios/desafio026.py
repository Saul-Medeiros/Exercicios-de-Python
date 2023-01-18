"""
Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A"
> Em que posição ela aparece a primeira vez
> Em que posição ela aparece a última vez.
"""
# deixa todas as letras da String maiúsculas e remove espaços indesejados:
frase = str(input('Digite uma frase: ')).upper().strip()
# conta quantas vezes o texto 'A' aparece na String:
print(f'Vezes em que a letra A aparece: {frase.count("A")}')
# procura qual a posição inicial do texto 'A':
print('Posição em que a letra A aparece na primeira vez: '
      f'{frase.find("A") + 1}')
# procura qual a posição final do texto 'A':
print('Posição em que a letra A aparece pela última vez: '
      f'{frase.rfind("A") + 1}')
