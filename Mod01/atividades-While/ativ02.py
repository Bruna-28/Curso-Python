"""
#Atividade 02:
 - Soma de Números de 1 a 100:
    Escreva um programa que use um laço while para
    somar os números de 1 a 100 e exiba o resultado.
"""

numero = 1
soma = 0
    
# Enquanto a soma passa pelos números de 1 a 100
    # A soma; adiciona +1 até chegar nos 100
while numero <= 100:
    soma += numero # Soma cada número percorrido
    numero += 1   
# Mostra todos os algarismos somados.   
print(f"A soma do números de 1 a 100 é: {soma}")