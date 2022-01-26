from cmath import sqrt
import math
ca_opos = float(input('Digite o valor do Cateto Oposto: '))
ca_adj = float(input('Digite o valor do Catet0o Adjasente: '))
hip = sqrt(pow(ca_opos, 2) + pow(ca_adj, 2))
print('Sendo o Cateto Oposto {} e o Cateto Adjasente {}, o valor da sua Hipotenusa de {}'. format(ca_opos, ca_adj, hip))
# "hipotenusa"

# resolução do Guanabara
ca_opos = float(input('Digite o valor do Cateto Oposto: '))
ca_adj = float(input('Digite o valor do Catet0o Adjasente: '))
hi = math.hypot(ca_opos, ca_adj)
print('O valor da hipotenusa é {:.2f}'.format(hi))