import os
import json
import subprocess

print("=== PROJETO FINAL - GUARDIÃO DE BATERIA ===\n")
nome = input("Qual seu nome? ")

# Pega a bateria do celular (vem em formato JSON)
try:
    resultado = subprocess.check_output(["termux-battery-status"]).decode("utf-8")
    dados = json.loads(resultado)
    bateria = dados['percentage']
    
    print(f"\nFala, {nome}! Sua bateria está em {bateria}%")

    if bateria <= 20:
        print("BATERIA BAIXA! Alerta máximo!")
        # Vibra 2 vezes forte
        os.system("termux-vibrate -d 1000")
        # Manda notificação vermelha
        os.system(f"termux-notification --title 'BATERIA BAIXA, {nome}!' --content 'Só {bateria}%, coloca pra carregar agora!' --priority high --vibrate 1000,1000,1000")
    
    elif bateria <= 50:
        print("Tá na metade, ainda dá pra codar.")
        os.system(f"termux-notification --title 'De boa' --content '{bateria}% - ainda aguenta mais uma aula'")

    else:
        print("Bateria cheia! Bora codar sem medo.")
        os.system("termux-notification --title 'Bateria de boa' --content '100%? Não, mas tá ótima pra programar!'")

except Exception as e:
    print("Não consegui ler a bateria. Você instalou o termux-api?")
    print(f"Erro: {e}")
    print("Roda: pkg install termux-api -y e instala o app Termux:API no F-Droid")

print("\nProjeto finalizado! Olha sua notificação.")
