usuarios = [['Ana'], ['Bruna'], ['Carlos']]

       
for usuario in usuarios:
    opcao = input("Qual o novo do usuário que deseja remover? ")
    if usuario[0] == opcao:
        print("Encontrado!")
        print(f"Usuário: {usuario[0]}")
        removendo = usuarios[0]
        break
    else:
        print("Não encotrado")
usuarios.remove(removendo)
print(f"Usuário: {usuarios}")