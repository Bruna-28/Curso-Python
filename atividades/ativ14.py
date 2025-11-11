"""
 #Atividade 14:
 - Verificar Status de Taxa de Desconto:
    Crie um programa que peça ao usuário o preço original de um produto e
    a quantidade comprada. Use if para verificar se a quantidade é maior que
    10 para aplicar um desconto de 10% sobre o total.
    
 - Calcula o total: preço × quantidade

 - Calcula o valor do desconto (porcentagem sobre o total)

 - Subtrai o desconto do total pra achar o preço final
"""

preco_produto = float(input("Digite o valor do produto: "))
qtd_produto = int(input("Qual a quantidade do que você vai levar? "))
total = preco_produto * qtd_produto 

qtdProduto_desconto = 10
percentual_desconto = 10

if qtd_produto > qtdProduto_desconto:
    
    print(total)
    valor_desconto = total * percentual_desconto / 100
    print(valor_desconto)
    desconto = total - valor_desconto 
    print(desconto)
else:
    