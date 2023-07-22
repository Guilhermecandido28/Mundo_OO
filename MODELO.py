class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    def __str__(self):
       return f'{self._nome} - {self.ano} - {self._like} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.duracao} min - {self.ano} - {self._like} Likes'


class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.temporadas} temporadas - {self.ano} - {self._like} Likes'

class Playlist:
    def __init__(self, nome,programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    def __add__(self, other):
        return self._programas.append(other)




vingadores = Filme('vingadores - guerra infinita', 2018, 160)
supernatural = Series('Supernatural', 2005, 15)
got = Series('game of thrones', 2008, 8)
topgun = Filme('Top Gun - Maverick', 2022, 230)
m8 = Filme('missão impossível - acerto de contas pt.1', 2023, 310)
filmes_series = [vingadores, supernatural, got, topgun]
meus_filmes = Playlist("meus filmes",filmes_series)
got.dar_like()
got.dar_like()
topgun.dar_like()
topgun.dar_like()
topgun.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
supernatural.dar_like()
supernatural.dar_like()

meus_filmes + m8
print(len(meus_filmes))

for programa in meus_filmes:
    print(programa)