#Script para baixar os datasets através de suas urls do Kaggle
#Imposta o módulo request para fazer a solicitação das urls
import requests
def download_file(url, dest_path):
    response = requests.get(url)
    with open(dest_path, 'wb') as file:
        file.write(response.content)

# URLs dos datasets
urls = {
    "sales_data": "https://www.kaggle.com/datasets/jehanzaibbhatti/sales_data.csv"
}

# Diretório de destino
data_dir = "data/"

# Baixar arquivos
for name, url in urls.items():
    dest_path = f"{data_dir}{name}.csv"
    download_file(url, dest_path)
    print(f"Downloaded {name} dataset successfully.")
    