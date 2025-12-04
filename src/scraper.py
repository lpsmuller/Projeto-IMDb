# scraper.py
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from classes import Movie 

def get_soup(url, user_agent):
    headers = {'User-Agent': user_agent}
    req = Request(url=url, headers=headers)
    html = urlopen(req).read()
    return BeautifulSoup(html, 'html.parser')

def extrair_filmes(url, user_agent, limite):
    """
    Retorna uma lista de OBJETOS da classe Movie.
    """
    soup = get_soup(url, user_agent)
    lista_objetos = []

    # Container principal da lista (pode variar se o site mudar)
    ul_list = soup.find('ul', class_='ipc-metadata-list')
    itens = ul_list.find_all('li', class_='ipc-metadata-list-summary-item')

    # Aplicamos o limite definido no config
    for item in itens[:limite]:
        try:
            titulo = item.find('h3', class_='ipc-title__text').text.strip()
            
            # Pega metadados (ano é geralmente o primeiro)
            metadata = item.find_all('span', class_='cli-title-metadata-item')
            ano = metadata[0].text.strip() if metadata else "N/A"
            
            nota = item.find('span', class_='ipc-rating-star--rating').text.strip()
            
            # Cria o objeto Movie
            novo_filme = Movie(titulo, ano, nota)
            lista_objetos.append(novo_filme)
            
        except AttributeError:
            continue
            
    return lista_objetos