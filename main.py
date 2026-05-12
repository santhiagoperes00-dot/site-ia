import os

# Limpa qualquer processo anterior e inicia o Streamlit na porta 8080
if __name__ == "__main__":
    os.system("python -m streamlit run app.py --server.port 8080 --server.address 0.0.0.0")
