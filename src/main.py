# main.py
import json
import scraper
import database
import analysis

def carregar_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def main():
    # 1. Carregar Configurações
    config = carregar_config()
    print(f"Configuração carregada. Buscando {config['n_filmes']} filmes...")

    # 2. Scraping (Coleta)
    # Retorna uma lista de objetos Python (Movie)
    catalogo_filmes = scraper.extrair_filmes(
        url=config['url'], 
        user_agent=config['user_agent'], 
        limite=config['n_filmes']
    )
    print(f"Coletados {len(catalogo_filmes)} filmes da internet.")

    # 3. Banco de Dados (Armazenamento)
    engine = database.iniciar_db(config['db_name'])
    database.salvar_catalogo(engine, catalogo_filmes)

    # 4. Análise de Dados (Inteligência)
    df_filmes = analysis.gerar_dataframes(engine)
    df_enriquecido = analysis.gerar_analise(df_filmes)

    # 5. Exportação
    if df_enriquecido is not None:
        analysis.exportar_arquivos(df_enriquecido)

if __name__ == "__main__":
    main()