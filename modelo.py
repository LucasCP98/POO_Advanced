class Programa:
    def __init__(self, nome, ano, avaliacao):
        self._nome = nome.title()
        self.ano = ano
        self.avaliacao = avaliacao
        self._likes = 0

    def dar_like(self):
        self._likes += 1
        return self._likes

    def estrelas(self):
        match self.avaliacao:
            case 1:
                self.avaliacao = "1⭐"
            case 2:
                self.avaliacao = "2⭐"
            case 3:
                self.avaliacao = "3⭐"
            case 4:
                self.avaliacao = "4⭐"
            case 5:
                self.avaliacao = "5⭐"

        return self.avaliacao

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes


class Filme(Programa):
    def __init__(self, nome, ano, avaliacao, duracao):
        super().__init__(nome, ano, avaliacao)
        self.duracao = duracao

    def __str__(self):
        return f"FILME: {self._nome} | ANO: {self.ano} | AVALIAÇÃO: {self.estrelas()} | " \
               f"LIKES: {self.dar_like()} | DURAÇÃO: {self.duracao}"


class Serie(Programa):
    def __init__(self, nome, ano, avaliacao, temporada):
        super().__init__(nome, ano, avaliacao)
        self.temporadas = temporada

    def __str__(self):
        return f"FILME: {self._nome} | ANO: {self.ano} | AVALIAÇÃO: {self.estrelas()} | LIKES: {self.dar_like()} | " \
               f"TEMPORADA: {self.temporadas}"


vingadores = Filme(nome="the avengers", ano=2018, avaliacao=5, duracao=160)
sintonia = Serie(nome="sintonia", ano=2019, avaliacao=3, temporada=5)

filmes_e_series = [vingadores, sintonia]
for programa in filmes_e_series:
    print(programa)
