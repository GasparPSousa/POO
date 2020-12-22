"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.


## Encapsular <- Cápsula



           Classe
_____________________________
/                            /
/         Atributos          /
/         Métodos            /
/                            /
/____________________________/

# Relembrando Atributos/Métodos Privados em Python.

Imagine que tempos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e
um método privado chamado de __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas Python não bloqueia
este acesso fora da classe. Com Python acontece o fenômeno chamado Name Mungling, que faz uma
alteração na forma de acessar os elementos privados, conforme:

_Classe__elemento

Exemplo:

instancia._Pessoa__nome

instancia._Pessoa__falar()


## Abstração

Em POO, Abstração é o ato de expor apenas dados relevantes de uma classe, escondendo os atributos e métodos privados
do usuário.

"""