class Programa:# class mãe
      def __init__(self, nome, ano, duracao):
         self._nome = nome.title() #_Programa__nome faria a conversão para não pegarem de fora 
         self.ano = ano
         self._likes = 0

      
      @property
      def likes(self):
         return self._likes

      def dar_like(self):
         self._likes += 1
      
      @property
      def nome(self):
         return self._nome
      
      @nome.setter
      def nome(self, novo_nome):
         self._nome = novo_nome.title()
      
class Filme(Programa):# Class filha
      def __init__(self, nome, ano, duracao):
         super().__init__(nome, ano)
         self.duracao = duracao
         
      
     

class Serie(Programa):# Class filha
      def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas  = temporadas


    
    
vingadores = Filme('Vingadores - Guerra infinita', 2018, 160 )
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

print(f' {vingadores.nome} -  {vingadores.ano} - {vingadores.duracao}: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
print(f'{atlanta.nome} - {atlanta.ano} -  {atlanta.temporadas} - {atlanta.likes}')
# novo jeito de formatar usado no python mais recente ao invés de colocar print( 'text {}'. format())
# se colocar o f na frente ex  print(f'nome: {nome variavel}')
# Por Herança a Class filha Herda alguns atribuos da Claas Mãe
#super() chama qualquer metodo da class mãe

