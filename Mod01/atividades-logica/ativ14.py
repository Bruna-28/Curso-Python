"""
#Atividade 14:
 - Verificar Status de Taxa de Desconto:
  Crie um programa que peça ao usuário o preço original de um produto e
  a quantidade comprada. Use if para verificar se a quantidade é maior que
  10 para aplicar um desconto de 10% sobre o total.
"""
linha = "=" * 50

# Esse é o percentual a mais de 10 unidades do produto.
percentual_qtdproduto = 10

qtd_produto = int(input("Digite a quantidade do produto que você deseja levar: "))

# bloco para caso o usuário digite valores negativos ou igual a zero.
if qtd_produto <= 0:
    print("Valor inválido!")
elif qtd_produto > 0:
    
    # Multiplicando o valor pelo produto
    preco_produto = float(input("Digite o valor do produto: "))
    
    print(linha)
    if preco_produto <= 0:
        print("Valor inválido!")
        print(linha)
        
    # Se quantidade do produto for menor que  10.
    else:
        # calculando preço pelo produto
        valor_total_qtd = preco_produto * qtd_produto
        #Será mostrado a quantidade, valor unitário e valor total do produto que será comprado.
        print(f"Quantidade: {qtd_produto} \nPreço: {preco_produto:.2f} \nValor total da cmpra: {valor_total_qtd:.2f}")
        print(linha) 
        
    # SeNão a quantidade do produto for maior que  10.
        if qtd_produto > 10:
        
            #Calcula a porcentageem em cima do produto.
            porcentagem_aplicada = valor_total_qtd * percentual_qtdproduto / 100
            print(f"Desconto aplicado {percentual_qtdproduto}% de desconto: R${porcentagem_aplicada}")
            print(linha)
        
            #Porcentagem sendo aplicada para o desconto do valor total dos produtos.
            valor_desconto_aplicado = valor_total_qtd - porcentagem_aplicada
            print(f"""
                Quantidade: {qtd_produto} 
                Preço unitário: R${preco_produto:.2f} 
                Valor total sem desconto: R${valor_total_qtd:.2f}
                Desconto ({percentual_qtdproduto}%): R${porcentagem_aplicada:.2f}
                Valor final a pagar: R${valor_desconto_aplicado:.2f}
                """)
            print(linha) 
  

    






