import random

# Função para escolha de golpes do adversário
def escolherGolpeIA(adversario, jogador):
    for golpe in adversario["golpes"]:
        if golpe["dano"] >= jogador["vidaAtual"]:
            return golpe

    return random.choice(adversario["golpes"])