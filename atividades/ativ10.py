"""
Atividade 10:
Verificar Nota para Aprovado:
    Crie um programa que peça a nota de um aluno e
    use if para verificar se ele foi aprovado (nota >= 6).
"""

nota_verificar = float(input("Digite a nota da redação: "))
media = 6

if nota_verificar >= media:
    print(f"A nota do aluno {nota_verificar}, aprovado!")
else:
    print(f"Nota {nota_verificar}, logo não alcançou a media {media}. Reprovado! ")