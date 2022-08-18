# #lista 2 parte
# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# print(teste)
# galera = list()
# galera.append(teste[:])#faz uma copia da estrutura e não uma ligação entre elas 
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)
    # galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45 ]]
    # print(galera[0])
    # print(galera[0][0])
    # print(galera[2][1])

    # for p in galera:
    #     print(f'{p[0]} tem {p[1]} anos de idade')
galera = list()# var composta
dados = list()# var composta
maior = menor = 0 # var simples da para fazer isso composta não
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
for p in galera: 
    if p[1]>= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1 
    else:
        print(f'{p[0]} é maior de idade.')
        menor += 1
print(f'temos {maior} maiores e {menor} menores de idades.')