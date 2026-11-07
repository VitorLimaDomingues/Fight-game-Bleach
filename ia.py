import random

# Função para escolha de golpes do adversário
def escolherGolpeIA(adversario, jogador, calcularDano, verificarCargas):
    golpesDisponiveis = []

    # Percorre o dicionário de golpes, e caso existe e tenha cargas, envia o valor para a lista golpesDisponiveis
    for golpe in adversario["golpes"]:
        if verificarCargas(golpe):
            golpesDisponiveis.append(golpe)

    # Percorre a lista de golpesDisponiveis para ver se um pode finalizar o player
    for golpe in golpesDisponiveis:
        danoEfetivo = calcularDano(adversario, jogador, golpe)

        if danoEfetivo >= jogador["vidaAtual"]:
            return golpe

    # Caso não tenha, escolhe uma habilidade que possui cargas e pode ser utilizada
    if golpesDisponiveis:
        return random.choice(golpesDisponiveis)

    return None