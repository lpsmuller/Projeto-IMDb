# classes.py

class TV:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} ({self.ano})"

class Movie(TV):
    def __init__(self, titulo, ano, nota):
        super().__init__(titulo, ano)
        self.nota = nota

    def __str__(self):
        return f"{super().__str__()} – Nota: {self.nota}"

class Series(TV):
    def __init__(self, titulo, ano, temporadas, episodios):
        super().__init__(titulo, ano)
        self.temporadas = temporadas
        self.episodios = episodios

    def __str__(self):
        return f"{super().__str__()} – Temporadas: {self.temporadas}, Episódios: {self.episodios}"