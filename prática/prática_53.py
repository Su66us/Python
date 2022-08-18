# Listas 
# são mutaveis 

lanche = ['hambúrguer', 'pizza', 'coca', 'pudim']
print(lanche)
lanche [3] = 'eu'
print(lanche)
num = [2,5, 9, 1]
num[2] = 3
# num.append(6)
# num.sort()#ordena os numeros 
# print(num)
# num.sort(reverse = True)# mostra de trás para frente
# print(num) 
# print(f'Essa lista tem {len(num)} elementos')
# num.insert(2, 0)#insere na posição 2 o numero zero
# print(num)
# num.pop(1)#remove apenas o numero que é colocado para o indice refazendo a lista
# print(num)
# num.insert(2, 2)#posição, numero que que adicionar
# print(num)
# num.remove(2)# remove  a primeira ocorrencia do numero 
# print(num)
# print(num)
# if 3 in num:
#     num.remove(3)
# else: 
#     print('Não achei o numero 3')
# print(num)
valores =[]
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')
    
# for c in valores:
#     print(f'{c}...',end = '')

# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encotrei o valor {v}...')

# a = [2, 3, 4, 7]
# b = a
# b[2] = 8
# o de cima cria uma ligação o de baixo cria uma copia 
#python iguala as listas cria uma conexção com elas
a = [2, 3, 4, 7]
b = a[:]# b vai receber copia dos valores de a
b[2] = 8
print(f'lista a: {a}')
print(f'lista b: {b}')