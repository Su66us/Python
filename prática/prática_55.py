#dicionarios 
# pessoas ={'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# # Na hora de referenciar elementos usa-se conchetes na hora de declaras usa-se chaves 
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# for k in pessoas.keys():
#     print(k)

# for k in pessoas.values():
#     print(k)

# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# lista com dicionario dentro
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São paulo', 'sigla': 'SP' }
# brasil.append(estado1)
# brasil.append(estado2)
# # print(estado1)
# # print(estado2)
# # print(brasil)
# print(brasil[0])
# print(brasil[1]['sigla'])
# print(brasil[0]['sigla'])
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())# não da para fazer o fatiamento usa-se o metodo interno ou seja [:] para o fatiomento não funciona dai usa-se o .copy
print(brasil)
for e in brasil:
    print(e)
    
for e in brasil:
    for k, v in e.items():
        print(f'o campo{k} tem o valor{v}')
for e in brasil:
    for v in e.values():
        print(v, end='')
    print()