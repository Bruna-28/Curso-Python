#contagem = 11

#while contagem > 1:
    #contagem -=1
    #print(contagem)
#print("Feliz ano novo!")

"""Atividade 04:
    ->Contagem Regressiva:
        Desenvolva um programa que use um laço while para exibir
        uma contagem regressiva de 10 até 1 e, em seguida, exiba
        "Feliz Ano Novo!"."""

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