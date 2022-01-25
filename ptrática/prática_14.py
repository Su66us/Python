from math import pow, sqrt
ca_opos = int(input('Digite o valor do Cateto Oposto: '))
ca_adj = int(input('Digite o valor do Catet0o Adjasente: '))
hip = sqrt(pow(ca_opos, 2) + pow(ca_adj, 2))
print('Sendo o Cateto Oposto {} e o Cateto Adjasente {}, o valor da sua Hipotenusa de {}'. format(ca_opos, ca_adj, hip))