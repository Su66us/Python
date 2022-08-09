import random


pessoa = int(input("Escalhas um numero de 0 a 5: "))
cont_pc =[0, 1, 2, 3, 4, 5]
escolha_pc = random.choice(cont_pc)
if pessoa == escolha_pc:
    print('Você é bom')
else:
    print('Computador venceu')