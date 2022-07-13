a = 0
impar_soma = 0

for x in range(0, 500):
    res = a * 3 
    if res % 3 == 0:
        print(res)
        impar_soma = res 
        impar_soma = impar_soma + impar_soma
    a +=1
print("a soma dos numeros impares de 0 a 500 que são multiplos de 3 é: {} ".format(impar_soma))