import random

def jogar():

    imprime_mensagem_abertura()

#Parte 1 do código = Leitura do arquivo para carregar uma palavra secreta aleatória.

    arquivo = open("palavras.txt", "r")
    palavras_lista = []

    for linha in arquivo:
        linha = linha.strip()
        palavras_lista.append(linha)

    arquivo.close()

    palavras_random = random.randrange(0, len(palavras_lista))
    palavra_secreta = palavras_lista[palavras_random].upper()

#Parte 2 do código = Lógica do jogo, organizar as letras da palavra acertada.

    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_faltando = str(letras_acertadas.count('_'))
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    print("encontrei a letra {} na posição {}".format(letra, index))
                index = index + 1
        else:
            erros = erros + 1  #Pode usar "erro += 1"
            print("Ops, você errou! Faltam {} tentativas.".format(7 - erros))
            desenha_forca(erros)

#Parte 3 do jogo = Define o fim do jogo.

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        letras_faltando = str(letras_acertadas.count('_'))
        print(letras_acertadas)
        print('Ainda faltam acertar {} letras'.format(letras_faltando))

#Parte 4 do jogo = Final do Jogo, imprimi a mensagem correta.

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
        print("A palavra secreta era", palavra_secreta, "!")

    print("Fim do Jogo!")

#LOCAL DAS FUNÇÕES - Que poderiam ser mais, quinem o professor fez.

def imprime_mensagem_abertura():
    print("***************************")
    print("Bem vindo ao jogo da forca!")
    print("***************************")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"): #Tem sempre que ser a última coisa do código. (ele engloba o resto)
    jogar()