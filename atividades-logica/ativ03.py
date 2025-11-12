"""
Atividade 03:
Verificação de Maioridade e Habilitação:
Crie um programa que peça a idade do usuário e se ele possui habilitação
(sim ou não). Use operadores lógicos para verificar se ele é maior de idade
(>= 18) e possui habilitação.

"""

idade = int(input("Digite a sua idade: "))
if idade < 18:
    print("Você é menor, logo não tem habilitação.") 
    
if idade >= 18:
    habilitado = input("Você possui habilitação? ").title()
    if habilitado == "Sim":
        print("Você é de maior, e possui habilitação.")
    elif idade >= 18 and habilitado != "Sim":
        print("Você é de maior, mas não possui habilitação.")
    else:
        print("Entrada inválida!")




"""
if idade < 18:
    print("Você é menor, logo não tem habilitação.") 
elif :
    print("Encerrado!")

elif idade >= 18:
    habilitado = bool(input("Você possui habilitação? ")) 
    if habilitado == "Sim":
        print("Você é de maior, mas não tem habilitação.")
elif idade >= 18 and habilitado == "Não":
    habilitado = bool(input("Você possui habilitação? ")) 
    print("Você é de maior, e tem habilitação.")
else :
    print("Respostas inválida.")
    
"""