#contagem = 11

#while contagem > 1:
    #contagem -=1
    #print(contagem)
#print("Feliz ano novo!")

# Executando o progrma de forma automatica.
while True:
    contando = int(input("Digite um número: "))
    
    #Verifica!
    #Se o número for menor ou igual a zero, 
    # falso segui para a proxima verificação. 
    if contando <= 0:
        print("Valor inválido!")
        print("Digite um valor maior que 0 (zero).")

    #SeNão: executa a contagem regressiva.   
    else:
        while contando > 0:
            contando -= 1
            print(contando)
            
        print("Boom!")
        break