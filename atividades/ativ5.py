"""
Atividade 05:

    # Desconto em Preço:
Peça ao usuário para inserir o preço de um produto e, em seguida,
use o operador de atribuição -= para aplicar um desconto de 5%.
"""

preco = float(input("Digite um preço para saber o seu descontonto: "))
porcetagem_fixa = 5
preco_fixo = 50
porCento_mult = 0

if preco < preco_fixo:
    porcent1 = porcetagem_fixa * 1

    if porCento_mult >= 0:
        print(f"Para o preço de {preco}, com {porcent1}%. ")
        porcentagem_desconto1 = (preco * porcent1) / 100
        preco_Desconto = preco - porcentagem_desconto1
        print(f"O novo valor com desconto é {preco_Desconto} com desconto de R${porcentagem_desconto1}")

if preco > preco_fixo:
    porcent2 = porcetagem_fixa * 2

    if porCento_mult >= 0:
        print(f"Para o preço de {preco}, com {porcent2}%. ")
        porcentagem_desconto2 = (preco * porcent2) / 100
        preco_Desconto = preco - porcentagem_desconto2
        print(f"O novo valor com desconto é {preco_Desconto} com desconto de R${porcentagem_desconto2}")

if preco > 500:
    porcent3 = porcetagem_fixa * 3
    if porcent3 == 15:
        print(f"Para o preço de {preco}, com {porcent3}%. ")
        porcentagem_desconto3 = (preco * porcent3) / 100
        preco_Desconto = preco - porcentagem_desconto3
        print(f"O novo valor com desconto é {preco_Desconto} com desconto de R${porcentagem_desconto3}")
    