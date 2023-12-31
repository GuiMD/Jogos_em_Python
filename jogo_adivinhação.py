def jogar():

    import random

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000
    pontos_perdidos = 10

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 8
    else:
        total_de_tentativas = 6

    while (rodada <= total_de_tentativas):
        print("Tentativa", rodada, "de", total_de_tentativas)
        chute_str = input("Tente advinhar o número entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou", chute)

        if(chute > 100 or chute < 1):
            print("Você não digitou um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = pontos_perdidos + (rodada * 11)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("O número secreto era", numero_secreto, "!")
    print("Fim do jogo!")

if(__name__ == "__main__"):     # Diz que se o código PRINCIPAL pediu a função, então ela será executada.
    jogar()
