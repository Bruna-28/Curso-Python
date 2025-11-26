
usuarios = []
linha = "=" * 50
#Controle de menu
while True:
    print("==== Menu ====\n")
    print("1 - Adicionar\n")
    print("2 - Verificar usuário\n")
    print("3 - Atualizar usuário\n")
    print("4 - Excluir usuário\n")
    print("5 - Sair\n")
    print(linha)
    
    option = input("Escolha uma opção: ")
    
    if not option.isdigit():   # verifica se NÃO é número
        print("Digite apenas números!")
        continue
    
    #Verificar se option está dentro das opções permitidas.
    if option not in ["1", "2", "3", "4", "5"]:
        print("Opção inválido!")
        continue
    
    print("Opção válido!")
               
    #Cadastrar um novo usuário.
    if option == "1":
        #Solicitando novos dados.
        nome = input("Digite seu nome: ").title()
        email = input("Digite seu email: ")
        
        print(linha)

        usuarios.append([nome, email])
        print(f"Nome: {nome}, \nEmail: {email}")
        
    #Verificar o usuário
    elif option == "2":
        procurar = input("Digite o nome que deseja encontrar: ").title()
        encontrado = False
        
        for usuario in usuarios:
            if usuario[0] == procurar:
                print("Usuário encontrado:")
                print(f"Nome: {usuario[0]}")
                print(f"Email: {usuario[1]}")
                print("=" * 60)
                encontrado = True
                break
        if not encontrado:
            print("Usuário não encontrado!")
            
    # Atualiza os dados do usuário   
    elif option == "3":
        procurar = input("Digite o nome do usuário que deseja atualizar: ").title()

        for usuario in usuarios:
            if usuario[0] == procurar:

                print("O que deseja atualizar?")
                print("Nome")
                print("Email")
                
                escolha = input("Opção: ")
                print(linha)

                # Atualizar nome
                if escolha == "Nome":
                    novoNome = input("Digite o novo nome: ").title()
                    usuario[0] = novoNome
                    print("Nome atualizado com sucesso!")
                    print(linha)
                    
                # Atualizar email
                elif escolha == "Email":
                    novoEmail = input("Digite o novo email: ")
                    usuario[1] = novoEmail
                    print("Email atualizado com sucesso!")
                    print(linha)


                break  # sai do for assim que atualizar
        else:
            print("Usuário não encontrado!")
    #elif option == "4":
           
            

            