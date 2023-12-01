import requests
import time

mercadela = "https://mercadela.onrender.com/categoria"
blogPessoal = "https://blogpessoal-backend.onrender.com/categoria"
while True:
    try:
        respostaMercadela = requests.get(mercadela)
        respostaBlogPessoal = requests.get(blogPessoal)

        if respostaBlogPessoal.status_code == 200:
            print("Requisição bem-sucedida!")
            print(respostaBlogPessoal.text)
        else:
            print(f"A requisição falhou com o código de status {
                  respostaBlogPessoal.status_code}")
        if respostaMercadela.status_code == 200:
            print("Requisição bem-sucedida!")
            print(respostaMercadela.text)
        else:
            print(f"A requisição falhou com o código de status {
                  respostaMercadela.status_code}")

    except Exception as e:
        print(f"Erro durante a requisição: {str(e)}")
    time.sleep(10)
