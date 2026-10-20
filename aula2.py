# Aula 2 - Variáveis e decisões

nome = input("Qual seu nome? ")
idade = input("Quantos anos você tem? ")

# O input sempre vem como texto, então temos que transformar em número
idade_numero = int(idade)

print(f"\nFala, {nome}! Você tem {idade_numero} anos.")

# Aqui o Python decide
if idade_numero >= 18:
    print("Você já é maior de idade. Pode codar sem limites!")
else:
    print("Você é menor de idade, mas já está na frente de muita gente.")

# Calcula em que ano nasceu
ano_atual = 2026
ano_nascimento = ano_atual - idade_numero
print(f"Você nasceu por volta de {ano_nascimento}.")
