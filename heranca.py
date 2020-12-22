"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. E também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outras classe
que passa a herdar atributos e métodos da classe herdada.

Entidade Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Entidade Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

## Nas classes Cliente e Funcionario, existe 1 método e 3 atributos iguais...

## Pergunta: Existem alguma Entidade genérica o suficiente para encapsular
os atributos e métodos comuns a outras Entidades??

## No exemplo em tela, a Entidade Pessoa seria adequada.

OBS: Quando uma classe herda de outra classe, ela herda TODOS atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe
    - Classe Mãe
    - Classe Pai
    - Classe Base
    - Classe Genérica

Quando uma classe herda de outra classe, ela é chamada de:
    [Cliente], [Funcionário]
    - Sub Classe
    - Classe Filha
    - Classe Específica



"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """ Cliente herda de Pessoa """

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # modo com faço acesso ao Construtor da Super Classe.
        self.__renda = renda


class Funcionario(Pessoa):
    """ Funcionario herda de Pessoa """

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula



cliente1 = Cliente('Cristina', 'Salles', '123.456.789-01', 20000)
funcionario1 = Funcionario('Gaspar', 'Sousa', '987.654.321-10', 50001)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())