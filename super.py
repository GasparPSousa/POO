"""
POO - O método super()

O método super() se refere a Super Classe.

Como o método super(), podemos fazer acesso a qualquer elemento(atributos/métodos e não somente o Construtor) da classe pai.

Uso o método super() na Sub Classe(classe filha/base) para acessar qualquer elemento da Super Classe(classe filha/específica)



"""

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}.')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        #Animal.__init__(self, nome, especie) # Possível
        super().__init__(nome, especie) # Esse é o Recomendado! Se eu utilizar o super(), não preciso passar
        # o self como parâmetro.
        super().faz_som('auauauaua')
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')

felix.faz_som('miau')