# analysis.py
import pandas as pd
import os

def gerar_dataframes(engine):
    """Lê do banco SQL e retorna DataFrames."""
    try:
        df_movies = pd.read_sql('SELECT * FROM movies', engine)
        # Converter nota para float
        if not df_movies.empty:
            df_movies['rating'] = df_movies['rating'].str.replace(',', '.').astype(float)
        return df_movies
    except Exception as e:
        print(f"Erro ao ler banco de dados: {e}")
        return pd.DataFrame()

def classificar_filme(nota):
    if nota >= 9.0: return "Obra-prima"
    elif nota >= 8.5: return "Excelente" # Ajustei para ter mais categorias
    elif nota >= 8.0: return "Muito Bom"
    else: return "Bom"

def gerar_analise(df):
    """Executa as transformações e exibe resumos."""
    if df.empty:
        print("DataFrame vazio. Nada a analisar.")
        return

    # 1. Cria categoria
    df['categoria'] = df['rating'].apply(classificar_filme)
    
    # 2. Resumo Pivot (Ano vs Categoria)
    resumo = pd.crosstab(df['year'], df['categoria'])
    resumo = resumo.sort_index(ascending=False)
    
    print("\n--- Análise: Filmes por Ano e Categoria (Top 10 anos) ---")
    print(resumo.head(10))
    
    return df # Retorna o DF modificado caso queira salvar

def exportar_arquivos(df):
    df.to_csv('relatorio_filmes.csv', index=False, sep=';', encoding='utf-8-sig')
    print("\nArquivo 'relatorio_filmes.csv' exportado com sucesso.")