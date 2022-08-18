# tuplas
# lanche = 'Hamburguer'
# lanche = 'pudim'
# print(lanche)
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim' )
#sendo o hambúrguer o lanche 0 o suco 1 a pizza 2 e o pudim 4 
#pode ser criado sem o uso de parenteses no novo python
# print(lanche[1:3])
# print(lanche[1:])
# print(lanche[-1])
# print(lanche[-3:])
# tuplas são imutavéis 
# lanche[1] = 'refrigerante'
# print(lanche[1])# dá erro
# print(len(lanche))
# for comida in lanche:
#     print(comida)

# mesma coisa que o de cima
# for cont in range(0, len(lanche)): com a posição 
#     print(cont)
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')
# print(sorted(lanche))# Coloca em ordem 
# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a
# print(len(c)) 
# print(c.count(5))# aparece quantas vezes o numero 5 aparece na tuplas
# print(c.count(9))
# print(c.index(8))# mostra a posição do numero, só pega a primeira ocorrencia ou seja a primeira vez que ele aparece
# print(c.index(4, 2))# mostra o 4 apartir da posição 2 c.- indica qual tupla vc quer que mostre
# print(c.index(2))
# print(c.index(2,4))
# print(c.index(5))
pessoa =('Gustavo', 39, 'M', 99.88)
# em tuplas funciona como vetores porém podendo mesclar str com num
#del(pessoa) comando del apaga a variavel 
# pode deletar a tupla inteira porem não consigo deletar um item da dupla 
print(pessoa)

