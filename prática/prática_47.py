a = int(input("Digite um numero: "))
b = 0
res = 0
print("  A tabuada")
for x in range (0, 11):
    res = a * b
    print("{} * {} = {}".format(a,b,res))
    b+=1
