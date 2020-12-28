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


conta1 = Conta('Gaspar', 3000, 5000)
conta2 = Conta('Cristina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# Caso eu queira somar os saldos das contas
soma = conta1._Conta__saldo + conta2._Conta__saldo
print(f'A soma do saldo das contas corrento do {conta1._Conta__titular} e da {conta2._Conta__titular} é R$ {soma},00.')
# Mas não é correto fazer acesso dessa forma. Você NUNCA deveria fazer acesso dessa forma!
# Só saiba que existe essa possibildiade, mas vc NUNCA deveria fazer esse acesso dessa forma num atributo PRIVADO.
# Se está declarado PRIVADO, é porque ele deve ser acessado somente DENTRO da classe. Essa é a REGRA!
# Para o próprio bem do sistema e bem do desenvolvedor, o ideal é que vc não faça acesse desse tipo.




