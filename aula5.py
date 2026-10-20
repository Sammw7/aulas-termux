import os
import time

print("Se prepara...")

# Faz vibrar por 1 segundo
os.system("termux-vibrate -d 1000")
time.sleep(1)

# Manda uma notificação de verdade no seu celular
os.system("termux-notification --title 'AULA 5' --content 'Seu programa me chamou!' --button1 'Fala comigo'")

# Mostra a bateria
print("\n--- Status do seu celular ---")
os.system("termux-battery-status")

print("\nOlha a barra de notificação lá em cima!")
