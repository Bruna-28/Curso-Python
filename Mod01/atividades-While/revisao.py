"""
# Funcionamento:

    O while verifica a condição
    antes de cada iteração.

    Se a condição for verdadeira,
    o bloco de código é executado.

    Se for falsa, o laço termina e a execução
    continua após o bloco while.

    É importante garantir que a condição
    eventualmente se torne falsa para
    evitar laços infinitos.

# APLICAÇÃO DO WHILE

    Iteração sobre Coleções:
    Percorrer elementos de listas, tuplas, conjuntos
    e dicionários 

    Automação de Tarefas Repetitivas:
    Executar tarefas repetitivas de forma eficiente.

    Processamento de Dados:
    Manipular e analisar grandes volumes de dados.

    Jogos e Simulações:
    Controlar o fluxo de jogos e simulações
    baseadas em condições variáveis.
"""

# =========== Funcionamento do While =========== 

# Um laço quee soma números até atingir um limite.
"""soma = 0
numero = 0

while numero <= 10:
    print(f"Soma inicial: {soma} \nNúmero inicial: {numero} ")
    print(f"Somando: {soma} + {numero} ")
    soma+=numero
    print(f"Resultado: {soma} ")
    
    numero += 1
    print(f"Próximo número: {numero}")
print(f"A soma dos número de 1 a 10 é: {soma}")
"""
#================================================================

"""Laço que conta de 1 a 10
contagem = 0

while contagem <= 9:
    print(f"Inicio:{contagem}")
    
    contagem += 1
    print(f"Passo:{contagem}")
print(f"Fim:{contagem}")
"""
#================================================================

# Soma de números de 1 a 100:

soma = 0
numeros = 0
while numeros <= 100:
    print(f"{soma} + {numeros}")
    
    soma += numeros
    
    print(f"Somados: {soma}")
    
    numeros += 1
    print(f"controlador de loop: {numeros}")
print(f"Resultado {soma}")