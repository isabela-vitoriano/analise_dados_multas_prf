# Importa bibliotecas
import requests
import gdown
from bs4 import BeautifulSoup
import zipfile
import os
from time import sleep
import shutil

url = 'https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf'  # URL da página da PRF que contém os arquivos CSV

# Faz uma requisição GET para a URL
response = requests.get(url)

# Obtém o conteúdo HTML da resposta
html_content = response.content

# Cria um objeto BeautifulSoup para analisar o conteúdo HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Localiza todos os links que possuem o atributo "title" contendo "infrações"
links = soup.find_all('a', {'title': lambda value: value and 'infrações' in value.lower()})

# Define anos de extração
anos = ['2020', '2021', '2022']

# Itera sobre os links e faz o download dos arquivos CSV para os anos desejados
for link in links:
    # Obtém o valor do atributo 'href' do link
    href = link.get('href')

    # Obtém o valor do atributo 'title' do link
    title = link.get('title')

    # Verifica se o link termina com a extensão '.csv' e se o título existe e contém 'infrações. Verifica se o título contém os anos desejados'
    if ('INFRAÇÕES' in title.upper()) and any(ano in title for ano in anos):
        print(title)
        
        output_zip = title + '.zip'  # Nome do arquivo zipado de saída
        output_dir = title + '_extraido'  # Diretório de saída para extrair os arquivos
        # Extrai o ID do arquivo do link compartilhado
        file_id = href.split('/')[-3]

        # Constrói a URL direta do arquivo para download
        download_url = f'https://drive.google.com/uc?id={file_id}'

        # Faz o download do arquivo em chunks usando a biblioteca requests
        response = requests.get(download_url, stream=True, params = {'confirm' : 1 })

        # Salva o arquivo zipado no disco
        with open(output_zip, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        # Extrai o conteúdo do arquivo zipado
        with zipfile.ZipFile(output_zip, 'r') as zip_ref:
            zip_ref.extractall(output_dir)

        # Remove os arquivos zipados
        os.remove(output_zip)

        extracted_folder = "arquivos_extraidos"  # Nome da pasta para armazenar os arquivos extraídos
        os.makedirs(extracted_folder, exist_ok=True) # Cria a pasta "arquivos_extraidos" se ela não existir

        # Move os arquivos extraídos para a pasta "arquivos_extraidos"
        for root, dirs, files in os.walk(output_dir):  # Itera sobre cada arquivo na lista
            for file_name in files:
                file_path = os.path.join(root, file_name)  # Caminho completo do arquivo
                relative_path = os.path.relpath(file_path, output_dir)  # Caminho relativo ao diretório de saída
                new_path = os.path.join(extracted_folder, file_name)  # Novo caminho completo para mover o arquivo
                os.rename(file_path, new_path)  # Move o arquivo para a pasta "arquivos_extraidos" usando o novo caminho
        
        # Verificar se o diretório raiz e seus subdiretórios estão vazios
        is_empty = True
        for dir_name in dirs:
            dir_path = os.path.join(output_dir, dir_name)
            if os.listdir(dir_path):
                is_empty = False
                break

        # Remover o diretório raiz se estiver vazio
        if is_empty:
            shutil.rmtree(output_dir)

        print(f'Download e extração de {title} concluídos.')