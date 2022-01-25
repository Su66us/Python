from math import sqrt, floor
# importando um parte  bliblioteca especifica  sem prescisar do uso do math 
a =  int(input('Digite um numero:  '))
raiz = sqrt(a)
print('Esse é o valor de {} sendo a raiz quadrada do seu número {}'.format(a, floor(raiz)))