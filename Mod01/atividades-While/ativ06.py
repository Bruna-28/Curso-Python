soma_total = 0
#Loop infinito com a condição de parada
while True:
    #Entrada de dados.
    numero_digitado = int(input("Digite um número: "))
    
    #Verifica se o número é negativo.
    if numero_digitado < 0:
        print("Escreva um número positivo!")
        break
    
    #Somado todos os números
    soma_total += numero_digitado
#Saida de dados.    
print(f"Todos os números somados: {soma_total}")      
    