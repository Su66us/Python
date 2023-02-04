#
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
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite    
        return valor_a_sacar <=  valor_disponivel_a_sacar 
        
    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('o Volor {} passou do limite'. format(valor))
    
    def tranfere(self,valor, destino):
        self.saca(valor)
        destino.saca(valor)
    
    @property
    def saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return '001'
    
    @staticmethod
    def codigo_banco():
        return {'BB' : '001', 'Caixa' : '104', 'Bradesco' : '237'}
# TODAS AS AÇÕES DENTRO DA CLASSE CONTA SÃO METODOS/ FUNCIONALIDADES
# responsabilidade tem que ser coesa com a classe  
#class receita de bolo para criar o objeto criado na de chamar a class memoria conta(referencia)= Conta(class)
# que é chamado de objeto
# atibuto class
# self.numero (vai) é a refencia do objeto
# conta.extrato() ,metodo
# metodo que devolve get_saldo
# get devolve set acessem 
