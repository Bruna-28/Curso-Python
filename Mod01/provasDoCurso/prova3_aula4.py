# Número secreto fixo
numero_secreto = 2

# Contador de tentativas
tentativas = 0
limite_tentativas = 3

# Loop de tentativas
while tentativas < limite_tentativas:
    # Pede o palpite do jogador
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break  # Sai do loop se acertar
    else:
        print("Errou! Tente novamente.\n")

# O else do while só é executado se o loop NÃO for interrompido por um break
else:
    print("Suas 3 tentativas acabaram. O número era", numero_secreto)
    print("Não desista! Tente novamente mais tarde!")
