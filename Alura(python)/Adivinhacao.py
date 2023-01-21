print("*********************************")
print("Bem vindo ao jogo da adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite um numero: ")

print('Você digitou' , chute_str)

chute = int(chute_str)
acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto
if (acertou):
    print('acertou')
else:
    if(maior):
        print('Você errou! O seu chute foi maior que o numero secreto.')
    elif(menor):
        print('Você errou! O seu chute foi menor que o numero secreto.')
# if == se
#else == se não
#elif == se não se


