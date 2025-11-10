num = float(input("Digite um número par ver o seu dobro: "))

if num > 0:
    num *= 2
    print(f"O valor do número solicitado em dobro: {num} ")
if num < 0:
    num *= 2
    print(f"O valor do número solicitado em dobro: {num} ")
else: 
    print("Fim do programa.")