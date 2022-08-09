import random
n1 = str(input('Digite nome: '))
n2 = str(input('Digite nome: '))
n3 = str(input('Digite nome: '))
n4 = str(input('Digite nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'. format(escolhido))