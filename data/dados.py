#Script para baixar os datasets através de suas urls do Kaggle
#Imposta o módulo request para fazer a solicitação das urls
import requests

def download_file( url, dest_path):
    response = requests.get(url)
    with open(dest_path, 'wb') as file:
        file.write(response.content)

# Aque especificamos as URLs dos datasets através de um dicionário

urls = {
    "sales_data": "https://example.com/sales_data.csv",
    "weather_data": "https://example.com/weather_data.csv",
    "real_estate_data": "https://example.com/real_estate_data.csv",
    "tweets": "https://example.com/tweets.csv",
    "survey_data": "https://example.com/survey_data.csv"

}

#Criamos uma variável que indicará o Diretório de destino

data_dir = "data/"

#Percorremos o dicionário e utilizamos o método para os baixar arquivos

for name, url in urls.items():
    dest_path = f"{data_dir}{name}.csv"
    download_file(url, dest_path)
    print(f"Downloaded {name} dataset successfully.")