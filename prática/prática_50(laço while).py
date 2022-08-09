# c = 1 
# while c <10:
#     print(c)
#     c = c + 1
#     # c += c vai pulando  
# print("fim")


# r = 'S'
# while r =='S':
#     n =int(input("Digite um valor: "))
#     r = str(input('Quer contiunuar?[S/N]')).upper()
# print("fim")

n = 1 
par = impar = 0
while n!= 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar+=1 
print('Você digitou {} númeors pares e {} números ímpares!'. format(par, impar))