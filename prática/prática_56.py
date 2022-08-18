# funções
# def lin():
#     print('-' *30)


# # programa principal (duas linha do de cima)
# # print('-'*30)
# # print(' curso em video ')
# # print('-'*30)
# # print('-'*30)
# # print('aprenda python')
# # print('-'*30)
# # print('-'*30)
# # print('João vitor')
# # print('-'*30)

# lin()
# print(' curso em video ')
# lin()
# lin()
# print('aprenda python')
# lin()
# lin()
# print('João vitor')
# lin()
#---------------------------------------------------------------------

# def titulo(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)

# # programa principal

# titulo('Bem vindo, João')

# def soma(a, b):
#     print(f'A = {a} e b = {b}')
#     s = a + b
#     print(s)

# # programa principal
# soma(5,5)
# # quando for especificar tem que ser os dois em especifico se não ele(python) não aceita
# soma(a = 5, b = 4)
# soma(a = 4, b = 5)
# # emapcotar parametro 
# def contador(* num):
#     print(num)

# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)
# def contador(* num):
#     for valor in num:
#         print(f'{valor} ', end='')
#     print('Fim')

# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def contador(*num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} numeros')
    

# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)
# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)
def soma(*valores): 
    s = 0 
    for num in valores:
        s+= num
    print(f'Somando os valroes {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)