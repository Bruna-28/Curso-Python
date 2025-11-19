"""
    2) Crie um programa que peça ao usuário um número 
    e informe se ele é positivo, negativo ou igual a zero. 
"""
# Entrada de valores
numero = int(input("Digite um número: "))
# Mensagem...
print(f"\nAnalisando o número {numero}...")

if numero == 0:
    print("Número neutro!")
elif numero > 0:
    print("Número positivo!")
else:
    print("Número negativo!")