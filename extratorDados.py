import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import math

# url de onde será extraído os dados
url = "https://www.ufrpe.br/br/lista-de-noticias"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \ (KHTML, like Gecko) Chrome / 86.6.4240.198Safari / 537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

# criando um dicionário para armazenar os dados que serão extraídos
quero = {'link': [], 'titulo': [], 'texto': []}

# pegando o número de páginas
for i in range(0, 3):
    url_pag = f'https://www.ufrpe.br/br/lista-de-noticias?page={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    link = soup.find_all('div', class_=re.compile(
        'views-field views-field-title'))


df = pd.DataFrame(quero)
df.to_csv('dados_uf.csv', index=False)
