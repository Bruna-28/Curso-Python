"""
Atividade 07:
Verificação de Caracteres em uma String:
Crie um programa que peça ao usuário uma frase e um caractere.
Use o operador de associação in para verificar se o caractere está
presente na frase.
"""
frase = input("Digite uma frase com caracter: ")
caracter = input("Digite uma caracter: ")

frase_caracter = frase + caracter

if caracter in frase_caracter:
    print(f"Sim! O caracter: {caracter} está na frase, e esta nessa forma: {frase_caracter}")
else:
    print("Programa encerrado!")

