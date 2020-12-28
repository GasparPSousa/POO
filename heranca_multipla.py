"""
POO - Herança Múltipla(HM)

Herança Múltipla nada mais é do que a possibilidade  de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos das classes herdadas.

#OBS: A HM, pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;


# Exemplo 1 - Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Mulderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3):
    pass



# Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
# todos os atributos e métodos das Super Classes

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

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())
print()

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())
print()

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) # ????? qual método cumprimentar ele vai executar?
# Tem a ver com o Method Resolution Order - MRO
# class Pinguim(Terrestre, Aquatico): Logo, o método cumprimentar utilizado será do método Terrestre
# que vem primeiro que Aquático na ordem dos parâmetros da class Pinguim.