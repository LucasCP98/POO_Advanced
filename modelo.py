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
        return f"SÉRIE: {self._nome} | ANO: {self.ano} | AVALIAÇÃO: {self.estrelas()} | LIKES: {self.dar_like()} | " \
               f"TEMPORADA: {self.temporadas}"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # Vale resltar que quando eu adiciono essa função (def __getitem__(self, item):) o python abilita a variavel
    # "playlist_fim_de_semana" abaixo ser interavel, caso contrario dará o erro: TypeError: 'Playlist' object is
    # not iterable, o nome dessa capacidade do python se chama: duck typing.
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def programas(self):
        return self._programas
    #
    # def __len__(self):
    #     return len(self._programas)


vingadores = Filme(nome="vingadores", ano=2018, avaliacao=5, duracao=160)
toy_story = Filme(nome="toy story", ano=1998, avaliacao=5, duracao=110)
velozes_e_furiosos = Filme(nome="velozes e furiosos", ano=2018, avaliacao=5, duracao=160)
bicho_vai_pegar = Filme(nome="bicho vai pegar", ano=2018, avaliacao=5, duracao=160)
madagascar = Filme(nome="madagascar", ano=2018, avaliacao=5, duracao=60)
sintonia = Serie(nome="sintonia", ano=2019, avaliacao=3, temporada=5)
naruto = Serie(nome="naruto", ano=2019, avaliacao=5, temporada=15)
pokemon = Serie(nome="pokemon", ano=2019, avaliacao=5, temporada=15)
blindspot = Serie(nome="blindspot", ano=2019, avaliacao=4, temporada=2)
scorpion = Serie(nome="scorpion", ano=2019, avaliacao=4, temporada=20)

filmes_e_series = [vingadores, toy_story, velozes_e_furiosos, bicho_vai_pegar, madagascar, sintonia, naruto, pokemon,
                   blindspot, scorpion]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)
print(f"Tamanho da Playlist fim de semana {len(filmes_e_series)} filmes e séries.")
for programa in playlist_fim_de_semana:
    print(programa)
