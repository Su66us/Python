
class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome
    
    @property # chama como propriedade sem o () ex: cliente.nome() antes de property// depois com o property cliente.nome
    def nome(self):
        print('Chamando @property nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('Chamando o setter nome()')
        self.__nome = nome