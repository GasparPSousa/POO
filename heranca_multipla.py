"""
POO - Herança Múltipla(HM)

Herança Múltipla nada mais é do que a possibilidade  de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos das classes herdadas.

#OBS: A HM, pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;

"""

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