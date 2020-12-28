""""
POO - MRO

Method Resolution Order(Resolução de Ordem de Métodos), é a ordem
de execução dos métodos(quem será executado primeiro)

Em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - via propriedade da classe __mro__
    - via método mro()
    - via help
    

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando...'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando...'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

tux = Pinguim('Tux')
print(tux.cumprimentar()) # ????? qual método cumprimentar ele vai executar?
# Tem a ver com o Method Resolution Order - MRO
# class Pinguim(Terrestre, Aquatico): Logo, o método cumprimentar utilizado será do método Terrestre
# que vem primeiro que Aquático na ordem dos parâmetros da class Pinguim.

"""

class Pinguim(Terrestre, Aquatico):
-> Eu sou Tux da terra!

class Pinguim(Aquatico, Terrestre):
-> Eu sou Tux do mar!

"""

print(Pinguim.mro())
print()
help(Pinguim)