from personagens import ichigo, ulquiorra, escolherPersonagem, escolherAdversario
from combate import lutar

def main():
    personagens = [ichigo, ulquiorra]

    jogador = escolherPersonagem(personagens)
    adversario = escolherAdversario(personagens)

    lutar(jogador, adversario)

if __name__ == "__main__":
    main()