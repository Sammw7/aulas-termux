# pergunta
favorito = input("qual seu jogo favorito? ")
horas = input("quantas horas por dia você joga? ")

# ação - transforma texto em número
horas_de_jogo = int(horas)
print(f"\nFalar, {favorito}! você joga {horas_de_jogo} horas por dia.")

# meio - decisão
if horas_de_jogo > 3:
    print("Viciado hein!")
else:
    print("Jogador equilibrado, respeito.")
