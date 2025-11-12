"""
#Atividade 11:
- Verificar Par ou Ímpar e Positivo ou Negativo:
    Escreva um programa que peça um número e use if para verificar
    se ele é par ou ímpar e também se é positivo ou negativo.

"""
number = int(input("Digite um número: "))

if number % 2 == 0 :
    print(f"Esse número {number}, é par!")
    if number > 0:
        print("Ele é um número positivo!")
    elif number < 0:
        print("Ele é um número  negativo!")
elif number % 2 != 0 :
    print(f"Esse número {number} é ímpar!")
    if number > 0:
        print("Ele é um número positivo!")
    elif number < 0:
        print("Ele é um número negativo!")
    

    