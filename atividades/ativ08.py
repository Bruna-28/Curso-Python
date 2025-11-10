"""
Atividade 08:
    Verificação de Palavras em uma Frase:
    Peça ao usuário para inserir uma frase e uma palavra.
    Use in para verificar se a palavra está na frase.
"""

frase = input("Digite uma frase: ")
palavra_verificar = input("Digite a palavra que deseja verificar se esta na frase: ")

if palavra_verificar in frase:
    print(f"A palavra está na frase!")
else:
    print("A palavra não está na frase")