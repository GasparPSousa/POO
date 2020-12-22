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

"""

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


cliente1 = Cliente('Cristina', 'Salles', '123.456.789-01', 20000)
funcionario1 = Funcionario('Gaspar', 'Sousa', '987.654.321-10', 50001)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())