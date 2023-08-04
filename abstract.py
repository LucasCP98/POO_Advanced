from abc import ABC
from numbers import Complex


# classes abstratas (abstract metodo), depois estudar mais, pois não entendi muito bem algumas partes. (Uso de ABCs)
class Playlist(Complex, ABC):
    pass


filme = Playlist()
