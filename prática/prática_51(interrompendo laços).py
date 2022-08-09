n = s = 0
while  True:
    n = int (input("Digite um número: "))
    if n == 999:
        break
    s+=n
print('a soma vale {}'.format(s))
# print(f'A soma vale {s}') outro jeito de formatar a string
# enquanto verdade
# flag/condição de parada 999 da o break no programa 
# s = n + n 
# dai formata 
nome = 'João'
idade = 33
salário = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}')