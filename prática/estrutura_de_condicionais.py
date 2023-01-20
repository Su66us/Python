nome = str(input('Digite seu nome: '))
nome_m = nome.upper()
print(nome_m)
if nome_m == 'JOÃO':
    print('Olá é um prazer, \033[35m{}\033[m '.format(nome))
else:
    print('erro')