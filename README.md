# Projeto-IMDb
Projeto IMDb Scraper and Analyzer - Este projeto realiza a extração automática (web scraping) dos filmes mais bem avaliados do IMDb, armazena os dados em um banco de dados relacional (SQL) e gera análises estatísticas sobre o ranking.

## 🚀 Funcionalidades

* **Scraping:** Coleta títulos, anos e notas do Top 250 do IMDb.
* **Modelagem:** Classifica os itens entre Filmes e Séries usando Orientação a Objetos.
* **Banco de Dados:** Salva os dados em SQLite usando SQLAlchemy (evita duplicatas).
* **Análise:** Gera DataFrames com Pandas e exporta relatórios em CSV/JSON.

## 📂 Estrutura do Projeto

* `src/`: Código fonte (scripts Python).
* `data/`: Banco de dados gerado e arquivos exportados (CSV, JSON).
* `config.json`: Parâmetros de configuração (URL, User-Agent, Limites).
