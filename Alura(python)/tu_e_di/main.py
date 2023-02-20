"""  idade1 = 39
idade2 = 30
idade3 = 70
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)
#lista sequencia de acesso aleatorio
lista = [39, 30, 70, 18]
print(len(lista))
print(lista) 
#objetos proprios
class ContaCorrente:
    def __init__(self, codigo):#iniciador
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):#metodo
        self.saldo += valor

    def __str__(self):#representação de string
        return f"[>>Codigo {self.codigo} Saldo {self.saldo} <<]"
    
    def deposita_para_todas(contas):
        for conta in contas:
            conta.deposita(100)
    
conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(47987)
conta_da_dani.deposita(1000)
print(conta_do_gui)
print(conta_da_dani)
contas =(conta_da_dani,conta_do_gui)
deposita_para_todas(contas)
#print(contas)

for conta in contas:
    print(conta)
 """
#lista[] uma sequencia de acesso aleatorio não pode dar posições para os itens nela
# tupla ()  é imutavel não pode adicionar ou remover coisa

"""Introdução a Collections

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xajf8Uy5Mm_1ZfpSHj5JaHtw9TiSgV0u
"""
""" 
idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39, 30, 27, 18]

type(idades)

len(idades)

idades[0]

idades

print(idades[1])
print(idades[2])
print(idades[3])

idades.append(15)

idades

idades[4]

idades[5]

for idade in idades:
  print(idade)

idades.remove(30)

idades

idades.remove(30)

idades.append(15)

idades

idades.remove(15)

idades

idades.append(27)
idades.remove(27)
idades

28 in idades

15 in idades

if 15 in idades:
  idades.remove(15)

idades

if 28 in idades:
  idades.remove(28)

idades

idades.append(19)
idades

idades.insert(0, 20)
idades

idades = [20, 39, 18]
idades

idades.append([27, 19])

idades

for elemento in idades:
  print("Recebi o elemento", elemento)

idades = [20, 39, 18]
idades.extend([27, 19])
idades

for idade in idades:
  print(idade + 1)

idades_no_ano_que_vem = []
for idade in idades:
  idades_no_ano_que_vem.append(idade+1)
idades_no_ano_que_vem

idades_no_ano_que_vem = [idade+1 for idade in idades]
idades_no_ano_que_vem

[idade for idade in idades if idade > 21]

idades

def proximo_ano(idade):
  return idade+1

[proximo_ano(idade) for idade in idades if idade > 21]

def faz_processamento_de_visualizacao(lista):
  print(len(lista))
  lista.append(13)

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)
idades

def faz_processamento_de_visualizacao(lista = []):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

def faz_processamento_de_visualizacao(lista = list()):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

def faz_processamento_de_visualizacao(lista = None):
  if lista == None:
    lista = list()
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
 """
"""# Objetos próprios"""
""" 
class ContaCorrente:
  
  def __init__(self, codigo):
    self.codigo = codigo
    self.saldo = 0

  def deposita(self, valor):
    self.saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)

conta_do_gui = ContaCorrente(15)
print(conta_do_gui)

conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
  print(conta)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]

print(contas[0])

conta_do_gui.deposita(100)

print(contas[0])

print(conta_do_gui)

print(contas[2])

contas[2].deposita(300)

print(conta_do_gui)

def deposita_para_todas(contas):
  for conta in contas:
    conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0,76)
print(contas[0], contas[1], contas[2])

deposita_para_todas(contas)
print(contas[0], contas[1], contas[2])

guilherme = ('Guilherme', 37, 1981) # tupla
daniela = ('Daniela', 31, 1987)
# paulo = (39, 'Paulo', 1979) # ruim

guilherme.append(6754)

conta_do_gui = (15, 1000)
# conta_do_gui.deposita() # variação OO
conta_do_gui[1]

conta_do_gui[1] += 100

def deposita(conta): # variação "funcional"(separando o comportamento dos dados)
  novo_saldo = conta[1] + 100
  codigo = conta[0]
  return (codigo, novo_saldo)

deposita(conta_do_gui)

conta_do_gui

conta_do_gui = deposita(conta_do_gui)
conta_do_gui

usuarios = [guilherme, daniela]
usuarios

usuarios.append(('Paulo', 39, 1979))

usuarios

usuarios[0][0] = 'Guilherme Silveira'

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(234876)
conta_da_dani.deposita(1000)

contas = (conta_do_gui, conta_da_dani)

for conta in contas:
  print(conta)

contas.append(423768)

contas[0].deposita(300)

for conta in contas:
  print(conta)

 """