import random

# Função para escolha de golpes do adversário
def escolherGolpeIA(adversario, jogador, calcularDano):
    for golpe in adversario["golpes"]:
        danoEfetivo = calcularDano(adversario, jogador, golpe)

        if danoEfetivo >= jogador["vidaAtual"]:
            return golpe

    return random.choice(adversario["golpes"])