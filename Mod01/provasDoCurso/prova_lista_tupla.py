"""
[PYIA-A01] 
    Crie uma lista contendo seis frutas de sua escolha. 
    Depois de ter a lista pronta, converta essa lista em uma tupla. 
    Por fim, exiba o conteúdo da tupla resultante para 
    verificar as frutas que foram armazenadas.
"""
#Lsita vazia
lista_frutas = [] 
tupla_frutas = ()

# Adicionando Fruta a uma lista de frutas
for i in range(6):
    fruta = input("Digite uma fruta: ")
    lista_frutas.append(fruta)
    
#Passando a lista para tupla
tupla_frutas = tuple(lista_frutas) 
print("=" * 80)

#saída
print(f"Lista de frutas: {lista_frutas}")
print("=" * 80)
print(f"Tuplas de frutas: {tupla_frutas}")
        
