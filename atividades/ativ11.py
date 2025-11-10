"""
#Atividade 11:
- Verificar Par ou Ímpar e Positivo ou Negativo:
    Escreva um programa que peça um número e use if para verificar
    se ele é par ou ímpar e também se é positivo ou negativo.

"""
number = int(input("Digite um número: "))

if number % 2 == 0 or number % 2 != 0:
    print(f"Esse número {number}, é par!")
    print(f"Esse número {number} é ímpar!")
elif number > 0 or number < 0 :
    print(f"É um número negativo!")
    print(f"É um número positivo!")

    