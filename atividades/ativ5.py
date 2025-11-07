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
        novo_preco = (preco * porcent1) / 100
        preco_Desconto = preco - novo_preco
        print(f"O novo valor com desconto é {preco_Desconto} com desconto de {porcent1}%")

elif preco > preco_fixo or preco < 500:
    porcent2 = porcetagem_fixa * 2

    if porCento_mult >= 0:
        print(f"Para o preço de {preco}, com {porcent2}%. ")
        novo_preco = (preco * porcent2) / 100
        preco_Desconto = preco - novo_preco
        print(f"O novo valor com desconto é {preco_Desconto} com desconto de {porcent2}%")

elif preco > 500:
    porcent3 = 15
    if porcent3 >= 0:
        print(f"Para o preço de {preco}, com {porcent3}%. ")
        novo_preco = (preco * porcent3) / 100
        preco_Desconto = preco - novo_preco
        print(f"O novo valor com desconto é {preco_Desconto} com desconto de {porcent3}%")
    