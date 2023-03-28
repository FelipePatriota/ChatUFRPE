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

    # for para pegar os links
    for l in link:
        links = l.find('a').get('href')
        quero['link'].append(links)    
   
    # for para pegar o título
    titulos = []
    for l in link:
        titulo = l.find('a').get_text().strip()
        titulos.append(titulo)
    quero['titulo'] += titulos

#For para extrair o texto
numero = len (quero['link'])
for i in range(numero):
    url_p = 'https://www.ufrpe.br/' + quero['link'][i]	
    site = requests.get(url_p, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    conteudo = soup.find('div', class_=re.compile('field field-name-body field-type-text-with-summary field-label-hidden'))
    texto = conteudo.find('p').get_text().strip()
    quero['texto'].append(texto)

df = pd.DataFrame(quero)
df.to_csv('dados_uf.csv', index=False)
