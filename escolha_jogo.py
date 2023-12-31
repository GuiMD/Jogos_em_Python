import jogo_forca
import jogo_adivinhação

def escolhe_jogo():
    print("*********************************")
    print("*********Escolha o jogo!*********")
    print("*********************************")

    print("(1) Jogo da Adivinhação (2) Jogo da Forca")

    jogo = int(input("Qual jogo deseja jogar? "))

    if(jogo == 1):
        print("jogo da adivinhação")
        jogo_adivinhação.jogar()
    elif(jogo == 2):
        print("jogo da forca")
        jogo_forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
