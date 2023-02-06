class Filme:
      def __init__(self, nome, ano, duracao):
         self.__nome = nome.title()
         self.ano = ano
         self.duracao = duracao
         self.__likes = 0
      
      @property
      def likes(self):
         return self.__likes
    
      def dar_like(self):
         self.__likes += 1

      @property
      def nome(self):
         return self.__nome 
      
      @nome.setter
      def nome(self, novo_nome):
         self.__nome = novo_nome.title()

class Serie:
      def __init__(self, nome, ano, temporadas):
         self.__nome = nome.title()
         self.ano = ano
         self.temporadas  = temporadas
         self.__likes = 0

      @property
      def likes(self):
         return self.__likes

      def dar_like(self):
         self.__likes += 1
      
      @property
      def nome(self):
         return self.__nome
      
      @nome.setter
      def nome(self, novo_nome):
         self.__nome = novo_nome.title()
    
    
vingadores = Filme('Vingadores - Guerra infinita', 2018, 160 )
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

print(f'nome: {vingadores.nome} - Ano: {vingadores.ano} - duração: {vingadores.duracao} - likes:{vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
print(f'nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - likes:{atlanta.likes}')
# novo jeito de formatar usado no python mais recente ao invés de colocar print( 'text {}'. format())
# se colocar o f na frente ex  print(f'nome: {nome variavel}')