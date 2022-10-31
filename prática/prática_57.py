# #docstrings
# #help()
# def contador(i,f,p):
#     """
#     -> faz uma contagem e mostra na tela
#     i: inicio da contagem
#     f: fim da contagem
#     p: passo da contagem
#     """
#     c = 1
#     while c <= f:
#         print(f'{c} ', end = ' ')
#         c += p
#     print('Fim')
# #parametro opcional 
# def contador(a=0, b=0, c=0):
#     """
#     -> faz a soma de três valores e mostra em tela
#     a: primeiro valor
#     b: segundo valor
#     c: terceiro valor
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
#escopo de variaveis
# def teste():
#     x = 8
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')

# #programa principal
# n = 2
# print(f'No porgrma principal, n vale{n}')
# teste()
# print(f'No program principal, x vale{x}')

# def funcao():
#     n1 = 4
#     print(f'N1 dentro vale{n1}')

# n1 = 2
# funcao()
# print(f'N1 fora vale{n1}')
#return comando 
def somar (a = 0, b = 0, c = 0):
    s  = a + b + c 
    return s 

r1 = somar(3 , 2,  5)
r2 = somar(2, 2)
r3 = somar(3)

print(f'Os resultados foram {r1}, {r2} e {r3}')