import os

# Inicia o servidor web do Streamlit na porta 8080 exigida pela Discloud
print("Iniciando o servidor da IA...")
os.system("streamlit run app.py --server.port 8080 --server.address 0.0.0.0")
