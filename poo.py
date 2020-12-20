"""
Programação Orientada a Objetos - POO

- POO é o paradigma de programação que utiliza mapeamento de objetos do mundo real
para modelos computacionais.

- Paradgma de programação é a forma/metodologia utilizada para pensar/desenvolver sistamas.

- Principais elementos de Orientação a Objetos
 - Classe <- Modelo do objeto do mundo real sendo represrntado computacionalmente.
 - Atributo <- Comportamento do Objeto.
 - Método <- Comportamento do Objeto (funções)
 - Construtor <- Método Especial utilizado para criar Objetos.
 - Objetos <- Instância da Classe.

"""
# A partir do momento que agente cria um classe, agente está criando no fundo, um novo tipo de dado.

numero = 10
print(numero)
print(type(numero))

nome = 'Gaspar'
print(nome)
print(type(nome))


class Produto:
    pass

ps4 = Produto()
print(ps4)
print(type(ps4))


