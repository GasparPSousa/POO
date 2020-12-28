"""
POO - Propriedades - Properties



"""

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'saldo de R$ {self.__saldo},00 do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -=valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite


conta1 = Conta('Gaspar', 3000, 5000)
conta2 = Conta('Cristina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# Caso eu queira somar os saldos das contas
soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas corrento do {conta1.get_titular()} e da {conta2.get_titular()} é R$ {soma},00.')
# Agora sim, fazendo acesso aos atributos PRIVADOS da forma correta!


# A melhor forma para termos acesso a métodos e atributos é criando métodos para manipulá-los.
# E chamamos esses métodos de GETTERS e SETTERS.
# GET significa PEGAR


