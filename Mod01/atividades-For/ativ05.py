<<<<<<< HEAD
#Resumo + exemplos:
"""
FOR + CONDICIONAIS:
    FOR: O for percorre cada item na sequência.
    CONDICIONAIS: as condicionais (if, elif, else) são
        verificadas e o bloco de código correspondente
        é executado.
    EXEMPLO 1: Imprimindo Números Pares de 1 a 10
     -> for i in range(1,11):
            if i % 2 == 0:
                print(f"{i} é par.")
                
# USANDO O LOOP FOR COM STRING:
Exemplo: Contagem de Vogais em uma String

texto = "Programação em Python."
contador_vogais = 0

for caractere in texto:
    if caractere.lower() in "aeiou":
        contador_vogais +=1
print(f"Números de vogais: {contador_vogais}")

 -> Explicação: Este loop
    for conta o número de
    vogais na string texto e
    imprime o total.
"""
#Atividade 05:
"""
#Atividade 05:
    Contagem de Números Positivos e Negativos:
        Escreva um programa que solicite ao usuário 10 números e use um
        laço for com uma condicional para contar quantos são positivos e
        quantos são negativos.
"""
contador_ = 0
contador_impares = 0

for i in range(1,11):
    if i > 0:
        num = int(input(f"Digite o número: "))
        if num <= 0:
            print("Entrada inválida!")
        elif num > 0:
            contador_pares +=1
        else:
            contador_impares += 1        
print(f"Números pares: {contador_pares}")
print(f"Números ímpares: {contador_impares}")
=======
listItens = []

while True:
    option = input(""" 
                   1 - Adicionar\n 
                   2 - Verificar Itens\n 
                   3 - Atualizar Itens\n 
                   4 - Excluir Itens\n 
                   5 - Sair
                   Escolha uma opção: """)
    match option:
        case "1":
            item = input("Digite o item que você deseja adiciona: ")
            listItens.append(item)
        case "2":
        # 1 - Método len - Usamos para saber o tamanho da lista
            print(f"Itens da lista: {(listItens.len())}")
        case "3":
            novoItem = input("Digite um novo item: ")
            position = int(input(f"Em qual posição dessas opções: {listItens.len()}"))
            listItens.insert(position, novoItem)
        case "4":
            removeItem = input(f"Qual item você deseja remover, desntro dessas opções: {listItens.len()}")
            listItens.remove(removeItem)
        case "5":
            if option == "Sair":
                print("Encerrado o programa!")
                break
>>>>>>> 46443a7b8974cfedee0cc4a5cee16a7935274d51
