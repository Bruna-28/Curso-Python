# Tipo de inteação para strings
"""palavra = "Infinity"

for letra in palavra:
    print(letra)"""
    
    
    
"""Atividade 01:
- Tabuada de um Número:
    Faça um programa que solicite um número ao usuário e use
    um laço for para exibir a tabuada desse número (de 1 a 10)."""
    
# Atividade 01: Tabuada de um Número

numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do número {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

        
    