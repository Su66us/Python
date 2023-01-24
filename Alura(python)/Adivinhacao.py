import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 100

    print('Qual nível de dificuldade?')
    print('(1) fácil (2) médio (3) Difícil')

    nivel = int(input("Defina o nivle: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5

    for rodada in range (1,total_de_tentativas + 1):
        #print('tentativa {} de {}' rodada, total_de_tentativas)
        print('tentativa {} de {}'.format( rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print('Você digitou' , chute_str)
        chute = int(chute_str)
        
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto
        if(chute < 1 or chute > 100):
            print('Você deve digitar um numero entre 1 e 100!')
            continue
        
        if (acertou):
            print('Você acertou e fez {} pontos'.format(pontos))
            print('acertou')
            break
        else:
            if(maior):
                print('Você errou! O seu chute foi maior que o numero secreto.')
            elif(menor):
                print('Você errou! O seu chute foi menor que o numero secreto.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        

    print('Fim de jogo')
# if == se
#else == se não
#elif == se não se
#-------------------
# while(enquanto isso é verdadeiro executa)
# formatação com {}