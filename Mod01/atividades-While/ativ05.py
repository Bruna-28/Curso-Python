"""Atividade 05:
    #Contagem até o Número Inserido:
        Crie um programa que solicite um número ao usuário e use
        um laço while para contar de 1 até o número inserido,
        exibindo apenas os números ímpares.
"""
inicio = 1
fim = int(input("Digite um número para saber os seus ímpares: "))

while inicio <= fim:
    
    if inicio % 2 != 0: 
       print(inicio)
    inicio += 1
