import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!      ")
    print("*********************************")

    arq = open("pal.txt", "r")
    palavras = []

    for linha in arq:
        linha = linha.strip()
        palavras.append(linha)

    arq.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)
    #  lista [] tuplas() não pode mudar imutavel estrura de dados
    # enquanto (true e true)

    while(not enforcou and not acertou):

        chute = input('Qual letra: ')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("Você ganhou!")
    else:
        print('Você perdeu!')
    print('Fim de Jogo!')
if(__name__ =="__main__"):
    jogar()