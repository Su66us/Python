
class Conta:
    
    def __init__(self,numero, titular, saldo, limite):
        print('Construindo objeto... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))
    def depositar(self, valor):
        self.__saldo += valor
    def saca(self, valor):
        self.__saldo -= valor
    def tranfere(self,valor, destino):
        self.saca(valor)
        destino.saca(valor)
    
        
# responsabilidade tem que ser coesa com a classe  
#class receita de bolo para criar o objeto criado na de chamar a class memoria conta(referencia)= Conta(class)
# que é chamado de objeto
# atibuto class
# self.numero (vai) é a refencia do objeto
# conta.extrato() ,metodo
