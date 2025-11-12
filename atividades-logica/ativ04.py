"""
Atividade 04:
Verificação de Notas Aprovadas:
Escreva um programa que peça duas notas de um aluno. Use operadores
lógicos para verificar se as duas notas são maiores ou iguais a 6.
"""

not1 = float(input("Digite a primeira nota: "))
not2 = float(input("Digite a segunda nota: "))

media = (not1 + not2) / 2
print(f"madia {media}")

if media >= 6:
    print(f"A media é {media}, então esta aprovado.")
else:
    print(f"A media é {media}, então está reprovado.")

    