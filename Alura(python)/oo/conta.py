
class Conta:
    
    def __init__(self,numero, titular, saldo, limite):
        print('Construindo objeto... {}'.format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
#class receita de bolo para criar o objeto criado na de chamar a class memoria conta(referencia)= Conta(class)
# que é chamado de objeto
# atibuto class
# self.numero (vai) é a refencia do objeto
