"""
POO - Atributos

Atributos <- Representam as características do Objeto. Ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

# Atributos de Instância: São atributos declarados dentro do Método Construtor.
# Eles podem ser Públicos ou Privados

OBS: Método Construtor: É um método especial para a construção do Objeto.

Médodo é uma função dentro de uma classe.

OBS: self nada mais é do que o objeto que está executando o método.
A palavra self é uma convenção utilizada por programadores em Python.
self é sempre o primeiro parâmetro.


"""

# Atributos de Instância:
# Em Python, o __init__ é o Método Construtor e é nele que fazemos as declarações dos atributos de instância.

# Em Python, o duplo underline __ tem o significado de privado, somente dentro da classe eu posso ter acesso.



# Classes com Atributos de Instância PÚBLICO.
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


# self é o próprio objeto
# Você está falando:
# O atributo voltagem do Objeto Lampada vai receber voltagem.
# O atributo cor do Objeto Lampada vai receber cor
# O atributo ligada do Objeto Lampada vai receber False.


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


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



# Atributos Públicos ou Atributos Privados.
# Agente está falando da VISIBILIDADE desses atributos
# Quando vc declara um atributo como PRIVADO, ele só pode ser acessado DENTRO da própria classe que ele foi declarado.

# Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é PÚBLICO.
# Ou seja, pode ser acessado em todo o projeto.
# Caso queiramos demonstrar  que determinado atributo deve ser tratado como PRIVADO, ou seja,
# que deve ser acessado/utilizado SOMENTE DENTRO da própria classe onde está declarado,
# utiliza-se duplo undersore no início de seu nome.

# Isso é conhecido também como Name Mangling.


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)
     # acessando atributo privado dentro da própria classe
    def mostra_email(self):
        print(self.email)


# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir
# que façamos acesso aos atributos sinalizados como PRIVADOS fora da classe.

# Exemplo

# user = Acesso('user@gmail.com', '123456')
#
# print(user.email)
# # print(user.__senha) # AtributeError - Isso é apenas um nível de segurança que Python coloca.
# print(dir(user))
# print(user._Acesso__senha) # Temos acesso, mas não deveríamos fazer esse acesso.
# # Essa junção do nome da classe com o nome do atributo privado(_Acesso__senha)  é um Name Mungling.
#
#
# user.mostra_senha()
# user.mostra_email()


# O que significa Atributo de Instância?

## Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

# user1 = Acesso('user1@gmail.com', '123456')
# user2 = Acesso('user2@gmail.com', '654321')
# # Duas Instâncias/Dois Objetos da classe Acesso. Ambos tem tanto email quanto senha.
#
# user1.mostra_email()
# user2.mostra_email()


# Atributos de Classe

# p1 = Produto('PlayStation 4', 'Video game', 2300)
# p2 = Produto('Xbox S', 'Video game', 4500)

# Atributos de Classe, são atributos que são declarados DIRETAMENTE na classe, ou seja, FORA do Construtor.
# Geralmente já inicializamos um valor e este valor é compartilhado entre todas as instâncias da classe.
# Ou seja, ao invés de cada instância da classe ter seus próprios valores como é o caso do "atributo de instância",
# com os "atributos de classe" todas as instâncias terão o mesmo valor para este atributo.

# Refatorar a classe Produto

class Produto:

    #Atributo de Classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0 # Inicializando o contador

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1 # Quando o objeto for criado, o objeto recebe no id, esse contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id  # Incremento do contador para que sempre pegue o próximo número e assim por diante.


p1 = Produto('PlayStation 4', 'Video game', 2300)
p2 = Produto('Xbox S', 'Video game', 4500)

print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe.
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe.

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe.

print(Produto.imposto) # Acesso correto de um atributo de classe.

print(p1.id)
print(p2.id)

# OBS: Em linguagens como Java, os atributos que conhecidos como atributos de classe aqui em Python,
# são chamados de atributos estáticos.

# Para os "atributos de classe", eles são alocados apenas uma vez na memória, independente da quantidade
# de objetos instânciados. Já os "atributos de instâncias", eles são alocados várias vezes a cada objeto
# instanciado.
