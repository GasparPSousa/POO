"""
POO - Objetos

Objetos <- São instâncias das classes. Ou seja, após o mapeamento do objeto do mundo real para a sua
representação computacional, podemos criar quantos objetos forem necessários. Podemos pensar nos
objetos/instâncias de uma classe como variáveis do tipo definido na classe.


"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Objetos/Instâncias
lamp1 = Lampada('branca', 110, 60)

lamp1.ligar_desligar() # A lampada está desligada e vai ser ligada.
lamp1.ligar_desligar() # A lampada está ligada e vai ser desligada.
lamp1.ligar_desligar() # A lampada está desligada e vai ser ligada.


print(f'A lâmpada está ligda? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 20000)

user1 = Usuario('Gaspar', 'Sousa', 'gasparufrj@gmail.com', '654321')
