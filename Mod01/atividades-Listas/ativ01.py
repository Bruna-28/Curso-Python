
usuarios = []
item = ""

#Controle de menu
while True:
    print("1 - Adicionar")
    print("2 - Verificar usuário")
    print("3 - Atualizar usuário")
    print("4 - Excluir usuário")
    print("5 - Sair")
    option = input("Escolha uma opção: ")
    
    #Verificar se option está dentro das opções permitidas.
    if option not in ["1", "2", "3", "4", "5"]:
        print("Opção inválido!")
    else:
        print("Opção válido!")
    #Cadastrar um novo usuário.
        if option == "1":
            #Solicitando novos dados.
            nome = input("Digite seu nome: ").title()
            email = input("Digite seu email: ")
            numberPhone = input("Digite seu telefone: ")

            usuarios.append([nome, email, numberPhone])
            print(f"Nome: {nome}, \nEmail: {email}, \nTelefone: {numberPhone}")
            
        #Verificar o usuário
        elif option == "2":
            procurar = input("Digite o nome que deseja encontrar: ").title()
            encontrado = False
            
            for usuario in usuarios:
                if usuario[0] == procurar:
                    print("Usuário encontrado:")
                    print(f"Nome: {usuario[0]}")
                    print(f"Email: {usuario[1]}")
                    print(f"Telefone: {usuario[2]}")
                    encontrado = True
                    break
            if not encontrado:
                print("Usuário não encontrado!")
            
        elif option == "3":
            update = input("Digite o que você deseja atualizar: ").title()
            encontrado = False
            
            for usuario in usuarios:
                if usuario[0] == update:
                    print("O que deseja atualizar?")
                    print("1 - Nome")
                    print("2 - Email")
                    print("3 - Telefone")
                    escolha = input("Opção: ")

                    # Atualizar nome
                    if escolha == "1":
                        novoNome = input("Digite o novo nome: ").title()
                        usuario[0] = novoNome
                        print("Nome atualizado com sucesso!")

                    # Atualizar email
                    elif escolha == "2":
                        novoEmail = input("Digite o novo email: ")
                        usuario[1] = novoEmail
                        print("Email atualizado com sucesso!")

                    # Atualizar telefone
                    elif escolha == "3":
                        novoTelefone = input("Digite o novo telefone: ")
                        usuario[2] = novoTelefone
                        print("Telefone atualizado com sucesso!")

                    else:
                        print("Opção inválida!")

                    encontrado = True
                    break

            if not encontrado:
                print("Usuário não encontrado!")