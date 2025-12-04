# database.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError
from classes import Movie, Series
import os

Base = declarative_base()

# Definição das Tabelas
class MovieDB(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    year = Column(String)
    rating = Column(String)

class SeriesDB(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    year = Column(String)
    seasons = Column(Integer)
    episodes = Column(Integer)

def iniciar_db(db_name):
    """
    Cria a engine e as tabelas (reseta se necessário para garantir estrutura).
    """

    engine = create_engine(f'sqlite:///{db_name}')
    # Opcional: drop_all para garantir que a estrutura esteja atualizada durante o desenvolvimento
    # Base.metadata.drop_all(engine) 
    Base.metadata.create_all(engine)
    return engine

def salvar_catalogo(engine, catalogo):
    """
    Recebe uma lista de objetos (Movie ou Series) e salva no banco.
    """
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("--- Iniciando Persistência no Banco ---")
    
    for item in catalogo:
        registro_db = None

        if isinstance(item, Movie):
            registro_db = MovieDB(title=item.titulo, year=item.ano, rating=item.nota)
        elif isinstance(item, Series):
            registro_db = SeriesDB(title=item.titulo, year=item.ano, seasons=item.temporadas, episodes=item.episodios)

        if registro_db:
            try:
                session.add(registro_db)
                session.commit()
                # print(f"Salvo: {item.titulo}") # Comentado para não poluir o terminal
            except IntegrityError:
                session.rollback()
                print(f"Duplicado (ignorado): {item.titulo}")

    session.close()
    print("--- Gravação Concluída ---")