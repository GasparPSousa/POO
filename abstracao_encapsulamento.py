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


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


# Testando

conta1 = Conta('Gaspar', 150.00, 1500)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

## Como o acesso está público, olha o que podemos fazer...

conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 999999999999999
conta1.limite = 9999999999999999999999999

print(conta1.__dict__)

## Logo, como o acesso está público, agente consegue não somente fazer a leitura, como
# também podemos alterar os dados. Com isso a segurança vai por água abaixo.
# Pq desse problema? Pois agente não encapsulou os dados conforme deveria.

conta1.extrato()