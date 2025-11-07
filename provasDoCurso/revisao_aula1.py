"""
    Crie um programa que pergunta o nome do
    usuário e exibe uma mensagem de boas-vindas personalizada.
"""
linha = "-" * 50

print(linha)

nome = input("Digite o seu nome: ")

print(f"Bem-vindo, {nome}!")

print(linha)

qtd_Horas_salario = float(input("Digite o valor de uma hora trabalhada: "))
horas_trablhada = int(input("Digite a quantidade de horas trabalhadas: "))

print(f"O salário total é de: R$ {qtd_Horas_salario * horas_trablhada}")
print(linha)

print(" #Operadores aritméticos: ")
x = 10
y = 19

print(f"x == y - {x == y}"
      f"\nx != y - {x != y}"
      f"\nx > y - {x > y}"
      f"\nx < y - {x < y}"
      f"\nx >= y - {x >= y}"
      f"\nx <= y - {x <= y}")

print(linha)

print(" #Operadores lógicos: ")
a = "true"
b = "false"

print(f"a and b - {a and b}")
print(f"a or b - {a or b}")
print(f"not a - {not a}")
print(f"not b - {not b}")

print(linha)

print(" #Operadores de atribuição: ")
x = 10

x += 20
print(f"x += 20 = {x}")

x -= 20
print(f"x -= 20 = {x}")

x *= 20
print(f"x *= 20 = {x}")

x /= 20
print(f"x /= 20 = {x}")

print(linha)

print(" #Operadores de associação: ")

listas_compras = "maçã" , "banana", "laranja", "uva"

verificando_lista = "maçã" in listas_compras
print(f"A maçã está na lista de compras? {verificando_lista}")

verificando_lista = "goiaba" not in listas_compras
print(f"A maçã está na lista de compras? {verificando_lista}")

verificando_lista = "Melão" not in listas_compras
print(f"O melão está na lista de compras? {verificando_lista}")

verificando_lista = "uva" in listas_compras
print(f"O melão está na lista de compras? {verificando_lista}")
