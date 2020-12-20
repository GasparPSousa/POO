"""
POO - Atributos

Atributos <- Representam as características do Objeto. Ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

# Atributos de Instância: São atributos declarados dentro do Método Construtor.

OBS: Método Construtor: É um método especial para a construção do Objeto.

Médodo é uma função dentro de uma classe.

OBS: self nada mais é do que o objeto que está executando o método.
A palavra self é uma convenção utilizada por programadores em Python.
self é sempre o primeiro parâmetro.


"""

# Atributos de Instância:
# Em Python, o __init__ é o Método Construtor e é nele que fazemos as declarações dos atributos de instância.

# Em Python, o duplo underline __ tem o significado de privado, somente dentro da classe eu posso ter acesso.



class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


# self é o próprio objeto
# Você está falando:
# O atribuoto voltagem do Objeto Lampada vai receber voltagem.
# O atributo cor do Objeto Lampada vai receber cor
# O atributo ligada do Objeto Lampada vai receber False.


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# self é o próprio objeto
# Você está falando:
# O Objeto Usuario no atributo nome, vai receber nome.
# O Objeto Usuario no atributo email, vai receber email.
# O Objeto Usuário no atributo senha, vai receber senha.

