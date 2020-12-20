"""
POO - Classes

Em POO, Classes nada mais são do que modelos do objetos do mundo real sendo representados computacionalmente.

Imagina que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos <- Representam as características do objeto. Ou seja, pelo atributos conseguimos representar
    computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente iríamos querer saber se a
    lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual a luminosidade dela e etc.

    - Métodos (funções) <- Representam os comportamentos do objeto. Ou seja, as ações que este objeto
    pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito
    provavelmente irìamos querer representar no nosso sistema é a açõa de ligar e desligar a mesma.


Em Python, para definirmos uma classe, usamos a palavra reservada class.

OBS: Utilizamos a palavra pass em Python quando temos um bloco de código que ainda não está implementado.

OBS: Quando nomeamos "nossas classes" em Python, utilizamos por convenção o nome inicial em maiúsculo.
Se o nome for composto, utiliza-se  as iniais de ambas as palavras em maiúsculo, todas juntas.
Mas as classes internas em python são em minúsculas. Desse forma fica fácil identificar o que é uma
classe interna do python e o que não é.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, clamamos
estes objetos que serão mapeados para classe de Entidades.


"""

idade = 32
print(type(idade))

preco = 2340.45
print(type(preco))

nome = "Gaspar P Sousa"
print(type(nome))

class Lampada:
    pass

lamp = Lampada()
print(type(lamp))


class ContaCorrente():
    pass


class Produto():
    pass


class Usuario():
    pass

class Int():
    pass


valor = int('42') # cast
print(help(int))  # O int nada mais é do que uma classe interna em python.

inteiro = Int()  # Esse Int é uma classe externa, criado por mim.
