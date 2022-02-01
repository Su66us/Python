from calendar import c
from re import M
from this import d


num = int(input('Digite um numero: '))
u = num // 1 % 10 
d = num // 10 % 10 
c = num // 100 % 10 
m = num // 1000 % 10 
print('O numero digitado foi {}'. format(num))
print('Unidade: {} '.format(u))
print('Dezena: {}'.format(d))
print('Centena: {} '.format(c))
print('Milhar: {} '.format(m))