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