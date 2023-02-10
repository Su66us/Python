
class Programa:# class mãe
      def __init__(self, nome, ano):
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

      def __str__(self):
         return f'{self._nome} - {self.ano} - {self._likes} Likes'
      
class Filme(Programa):# Class filha
      def __init__(self, nome, ano, duracao):
         super().__init__(nome, ano)
         self.duracao = duracao
         
      def __str__(self):
         return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'
      
     

class Serie(Programa):# Class filha
      def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas  = temporadas

      def __str__(self):
         return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

class Playlist:
   def __init__(self, nome, programa):
      self.nome = nome
      self._programa = programa

   def __getitem__(self, item):
      return self._programa[item]


   @property
   def listagem(self):
      return self._programa
   
   
  
   def __len__(self):
      return len(self._programa)      




vingadores = Filme('Vingadores - Guerra infinita', 2018, 160 )
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
vingadores.dar_like()
vingadores.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]#lista
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist? {len(playlist_fim_de_semana)}')



for programa in playlist_fim_de_semana:
   print(programa)


#print(f'tá ou não tá? {demolidor in playlist_fim_de_semana}')


# if hasattr(programa, 'duracao'):
   #   detalhes = programa.duracao
# else: 
   #  detalhes = programa.temporadas # verificar se tem o atributo na lista



# novo jeito de formatar usado no python mais recente ao invés de colocar print( 'text {}'. format())
# se colocar o f na frente ex  print(f'nome: {nome variavel}')
# Por Herança a Class filha Herda alguns atribuos da Claas Mãe
#super() chama qualquer metodo da class mãe

