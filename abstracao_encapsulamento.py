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



print(conta1.numero) # Agora os atributos estão privados, nem leitura mais consigo fazer.
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

# Como o acesso agora está privado, além de não conseguir fazer a leitura, não conseguimos fazer alteração.

conta1.numero = 42 # Agora os atributos estão privados, nem leitura mais consigo fazer.
conta1.titular = 'Xuxa'
conta1.saldo = 999999999999999
conta1.limite = 9999999999999999999999999

conta1.extrato()


# Logo, como agora o acesso está privado, agente consegue "não" consegue fazer nem leitura e muito menos conseguimos
# alterar os dados. Com isso a segurança "melhora".
# Só de tornar os atributos privados, já temos nossa conta protegida sem "nenhum" problema de infração.


## Embora, lembrando novamente, que a linguagem Python não impede agente de fazer acesso aos dados.
# Está na mão do programador, do desenvolvedor.

print(conta1._Conta__titular) # Name Mungling
conta1._Conta__titular = 'Zico'
print(conta1.__dict__)

"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')


    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo Insuficiente')
        else:
            print('O valor deve ser positivo')


# Testando

conta1 = Conta('Gaspar', 150.00, 1500)
print(conta1.__dict__)

conta1.depositar(150)
print(conta1.__dict__)

conta1.sacar(2000)
print(conta1.__dict__)
