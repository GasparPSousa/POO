"""
POO - Métodos

- Métodos (funções) <- Representam comportamentos do objeto. Ou seja, as ações que esse objeto
pode realizar no seu sistema.
_ Métodos nada mais são que funçoes dentro de uma classe.

Em Python, dividimos os métodos em 2 grupos:
    - Métodos de Instância
    _ Métodos de Classe


    # Métodos de Instância

    Por que método de Instância? Pq precisamos de uma instância da classe para utilizá-lo.
                                Pq precisamos de uma instância do objeto para poder fazer acesso a ele.
    É um método que está dentro da prória classe.

    Fazemos acesso aos atributos de instância.


    # Métodos de Classe

    Mesma ideia dos atributos de classe.

    Os métodos de classe não estão vinculados a nenhuma instância da classe, mas sim diretamente a ela.

    Uma diferença aqui nos métodos de classe em relação aos atributos de classe, é que na declaração
    desses métodos, agente utiliza um DECORATOR para indicar que o método é de classe e não de instância.

    São conhecidos como "métodos estáticos" em outras linguagens.

    Não fazemos acesso aos atributos de instância.



O método dunder init __init__ é um objeto especial chamado de construtor e sua função é
contruir o objeto a partir da classe.

OBS: Todo elemento em Python que "inicia E finaliza" com duplo underline é chamado de dunder(Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de Métodos Mágicos.

ATENÇÃO!! Por mais que possamos criar nossas próprias funções utilizando dunder(underline no início e no fim),
não é aconselhado. Python possui vários métodos com essa forma de nomeclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da linguagem. Então, evite ao máximo! De preferência, NUNCA o faça.


# Em Python, Métodos são escritos em letras minúsculas.
Se o nome for composto, o nome terá as palavras separadas por underline.

"""



class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """ Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100
        # A função do self aqui é pegar o produto em si.


# Fizemos a instalação usando o.... pip install passlib
# Para fazer a criptografia da senha.
# O tipo sha256 é extremamente poderoso.

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod #decorator
    def conta_usuarios(cls): # O primeiro parâmetro não é o self, mas sim o cls, que é a própria classe.
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema ')

    @classmethod
    def ver(cls):
        print('Teste')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        # rounds vai fazer 200000 embaralhamentos. Qto mais embaralhado, mais a chance da senha ser forte.
        # salt_size é o tamanho da parte do texto que será juntado a outro para criptografar.
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')


    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]




p1 = Produto('Play Station 4', 'Video game', 2300)

# print(p1.desconto(20))
# # Pq precisamos de uma instância do objeto para poder fazer acesso a ele.
#
# # print(Produto.desconto(40)) # Dá Erro, pq ela não tem valor,não tem objeto.
#
# print(Produto.desconto(p1, 20)) # Agora conseguimos fazer pela classe, esse p1 é o próprio objeto.
# # self, desconto e o self é o próprio objeto em si.

print()

# user1 = Usuario('Gaspar', 'Sousa', 'gasparufrj@gmail.com', '123456')
# user2 = Usuario('Cristina', 'Salles', 'salles@gmail.com', '654321')
#
# print(user1.nome_completo()) # Aqui o self é o user1. Aqui estou usando a instância user1
# print(user2.nome_completo()) # Aqui o self é o user2. Aqui estou usando a instância user2
#
# print(Usuario.nome_completo(user1)) # Aqui estou usando a Classe e a classe não tem self, ela não tem instância,
# # então passei o self user1 como parâmetro.
# print(Usuario.nome_completo(user2)) # Aqui estou usando a Classe e a classe não tem self, ela não tem instância,
# # então passei o self user2 como parâmetro.
#
# print()
#
# print(f'Senha User 1: {user1._Usuario__senha}') # Acesso de forma errada de um atributo de classe.
# print(f'Senha User 2: {user2._Usuario__senha}') # Acesso de forma errada de um atributo de classe.


# nome = input('Informa o nome: ')
# sobrenome = input('Informa o sobrenome: ')
# email = input('Informe o e-mail: ')
# senha = input('Informe a senha: ')
# confirma_senha = input('Confirme a senha: ')
#
# if senha == confirma_senha:
#     user = Usuario(nome, sobrenome, email, senha)
# else:
#     print('Senha não confere....')
#     exit(42)
#
# print('Usuário criado com sucesso!')
#
# senha = input('Informe a senha para acesso: ')
#
# if user.checa_senha(senha):
#     print('Acesso permitido')
# else:
#     print('Acesso negado')
#
# print(f'Senha User Criptografada: {user._Usuario__senha}')  # Acesso errado!
# # Essa senha criptografa que armazenamos nos BD...não é o texto puro, agente nem vê o texto puro
# # que o usuário digita. Por isso as senhas criptografadas são salvas nos BD, é uma questão de segurança.


# Métodos de Classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456') # Acessando o método privado dentro da classe.

# Usuario.conta_usuarios() # Forma correta de acesso. Via o nome da classe.
# user.conta_usuarios() # Possível, mas incorreta. Via a instância da classe.
#
# Usuario.ver()

#print(user.__gera_usuario()) # Vai dar erro, pois não tenho acesso ao método privado.
print(user._Usuario__gera_usuario()) # Acesso de forma ruim.