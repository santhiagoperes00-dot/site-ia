import os
import sys

# Define o comando para rodar o streamlit
cmd = "streamlit"
args = [
    "streamlit", "run", "app.py",
    "--server.port", "8080",
    "--server.address", "0.0.0.0",
    "--server.headless", "true"
]

print("🚀 Iniciando a IA Edson Omni...")

# O execvp substitui o processo atual pelo processo do streamlit.
# Isso evita que o processo do python original fique "travando" a Discloud.
os.execvp(cmd, args)
