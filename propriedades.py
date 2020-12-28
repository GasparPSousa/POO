"""
POO - Propriedades - Properties

Em linguagem de programação como o JAVA, ao declararmos ATRIBUTOS PRIVADOS nas classes,
costumamos a criar MÉTODOS PÚBLICOS para manipulação desses atributos. Esses métodos
são conhecidos por getters e setters, onde os getters RETORNAM o valor do atributo
e os setters ALTERAM o valor do mesmo.



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

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Gaspar', 3000, 5000)
conta2 = Conta('Cristina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# Caso eu queira somar os saldos das contas
soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas corrento do {conta1.get_titular()} e da {conta2.get_titular()} é R$ {soma},00.')
# Agora sim, fazendo acesso aos atributos PRIVADOS da forma correta!
print()
print(conta1.__dict__)
conta1.set_limite(999999)
print(conta1.__dict__)
# O set recebe um parâmetro e ALTERA o valor do atributo.


# A melhor forma para termos acesso a métodos e atributos é criando métodos para manipulá-los.
# E chamamos esses métodos de GETTERS e SETTERS.
# GET significa PEGAR
# SET significa ALTERAR


Esses getters e setters é mais estilo JAVA, para Python, utilizamos Properties!

"""

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    # Se agente quiser criar um set para um atributo, agente vai criar um decorato com o mesmo nome do atributo.
    def limite(self, novo_limite):
        self.__limite = novo_limite


    def extrato(self):
        return f'saldo de R$ {self.__saldo},00 do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -=valor
        destino.__saldo += valor

# Eu gosto sempre de programar nessa ordem:
    # Atributos de classe
    # Construtores e seus Atributos de Instância
    # Property
    # Métodos de Instância

# Sempre nessa ordem...é apenas uma sugestão.


conta1 = Conta('Gaspar', 3000, 5000)
conta2 = Conta('Cristina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# Caso eu queira somar os saldos das contas
soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas corrento do {conta1.titular} e da {conta2.titular} é R$ {soma},00.')
# Agora sim, fazendo acesso aos atributos PRIVADOS da forma correta!
print()

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)


# A melhor forma para termos acesso a métodos e atributos é usando Property para manipulá-los.
# É quase como se fosse um método, mas por causa do decorator @property, fazemos o acesso SEM os parênteses.
# A partir do momento que usamos o decorator @property, é como se fosse o método GET.
# Por padrão, uma propriedade é um GET.

# Se agente quiser criar um set para um atributo, agente vai criar um decorato com o mesmo nome do atributo.







