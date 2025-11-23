"""Atividade 05:
    #Contagem até o Número Inserido:
        Crie um programa que solicite um número ao usuário e use
        um laço while para contar de 1 até o número inserido,
        exibindo apenas os números ímpares.
"""
number = 0
numberUser = int(input("digite um número: "))

while number < numberUser:
    
    resto = numberUser % 2 == 0
    
    if numberUser % 2 == 0:
        resto += numberUser
print(f"Número Ímpares: {numberUser}")       