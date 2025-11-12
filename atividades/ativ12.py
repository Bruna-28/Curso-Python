"""
 #Atividade 12:
 - Verificar Classificação de IMC:
    Crie um programa que calcule o Índice de Massa Corporal (IMC)
    e use if para classificar o resultado em:
    "Abaixo do peso",
    "Peso normal",
    "Sobrepeso" e "Obesidade".
"""
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a seu altura: "))

IMC = peso / altura**2 
print(f"IMC: {IMC:.2f}")

abaixo_peso = 18.5
peso_normal = 24.9
sobrepeso = 29.9
obesidade_I = 34.9
obesidade_II = 39.9


if IMC < abaixo_peso:
    print(f"Você está abaixo do peso com IMC: {IMC:.2f}")
elif IMC <= peso_normal:
    print(f"Você está no peso normal, com IMC: {IMC:.2f}")
elif IMC <= sobrepeso:
    print(f"Você está com sobrepeso, com IMC: {IMC:.2f}")
elif IMC <= obesidade_I:
    print(f"Você está com obesidade grau I, com IMC: {IMC:.2f}")
elif IMC <= obesidade_II:
    print(f"Você está com obesidade grau II, com IMC: {IMC:.2f}")
else:
    print(f"Você está com obesidade grau III, com IMC: {IMC:.2f}")