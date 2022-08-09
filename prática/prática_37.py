idade = int(input('Digite a sua idade: '))
if idade <= 9 :
    print(idade,'sua catgoria é a MIRIM')
elif idade <= 14 and idade > 9:
    print(idade,'Sua categoria é a INFANTIL')
elif idade <= 19 and idade> 14:
    print(idade,'Sua categoria é a JUNIOR') 
elif idade <= 25 and idade> 19:
    print(idade,'Sua categoria é a SÊNIOR')
else:
    print(idade,'Sua categoria é a MASTER')