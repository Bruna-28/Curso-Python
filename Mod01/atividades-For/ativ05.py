
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

for i in range(1,11):
    numerDoUsuario = int(input("Digite um número: "))
    i += 1 
    print(i)
    if numerDoUsuario < 0 and numerDoUsuario > 0:
        numerDoUsuario+=i
        print(f"Números positivos: {numerDoUsuario}")
        
        numerDoUsuario+=i
        print(f"Números negativos: {numerDoUsuario}")   

    
                