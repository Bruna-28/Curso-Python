"""
#Atividade 13:
 - Sistema de Login Simples:
    Desenvolva um programa que peça ao usuário um nome de usuário
    e uma senha e use if para verificar se são iguais a "admin" e "1234", respectivamente."""
    
nome_usuario = input("Digite o nome do usuário: ")
senha_usuario = int(input("Digite a senha do usuário: "))

if nome_usuario != senha_usuario:
    print("Bem-vindo!")
else:
    print("Acesso negado!")