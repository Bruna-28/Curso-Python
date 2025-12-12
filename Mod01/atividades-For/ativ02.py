"""Atividade 02:
- Soma de Números de 1 a 100:
    Crie um programa que use um laço for para somar
    todos os números de 1 a 100 e exiba o resultado."""
    

soma = 0  
for i in range(1, 101):# 1, 101, mas conta 100 números.
    soma+=i
print(f"A soma de todos os números é: {soma}")

"""✔️ Explicação rápida
 - range(1, 101) → vai de 1 até 100 (o 101 não entra na contagem).
 - soma += i → soma cada número de i dentro do loop.
 - Resultado final = 5050."""