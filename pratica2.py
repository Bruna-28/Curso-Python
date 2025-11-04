"""
Atividade 01:
Comparação de Idades:
Peça ao usuário duas idades e use operadores de comparação para
verificar se a primeira idade é maior, menor ou igual à segunda.
"""
idade1 = int(float(input("Digite a primeira idade: ")))
idade2 = int(float(input("Digita a segunda idade: ")))

if idade1 > idade2: 
  print(f"{idade1} anos é maior que {idade2} anos!")

elif idade1 < idade2:
  print (f"{idade1} anos é menor que {idade2} anos!")

else: 
  print(f"{idade1} anos é igual {idade2} anos!")





  """  Atividade 02:
Verificar Igualdade de Strings:
Peça ao usuário duas palavras e use operadores
de comparação para verificar se elas são iguais.
"""

string1 = input("Digite a primeira palavra: ")
string2 = input("Digite a segunda palavra: ")

if string1 == string2:
  print(f"A primeira palavra é igual a segunda palavra.")
else:
  print(f"A primeira palavra é diferente da segunda palavra.")