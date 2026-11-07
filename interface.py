# Função exibir informação dos personagens
def informacaoDosPersonagens(personagem):

    print("=" * 35)
    print(" " * 10 + f"{personagem["nome"]}")
    print("=" * 35)
    print(f"Vida: {personagem["vidaMaxima"]} | Ataque: {personagem["ataque"]} | Defesa: {personagem["defesa"]}\n")

    print("HABILIDADES")
    print("-" * 30)
    for golpe in personagem["golpes"]:
        print(f"- {golpe['nome']} | Dano: {golpe['dano']}")
    print("-" * 30)

# Função para exibir HP (health points) dos personagens
def informacaoDaVidaDosPersonagens(personagem):
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    VERMELHO = "\033[31m"
    RESET = "\033[0m"

    tamanhoDaBarra = 20 # Define tamanho da barra
    proporcao = personagem["vidaAtual"] / personagem["vidaMaxima"] # faz o cálculo da divisão da vida atual pela vida máxima
    
    blocosPreenchidos = int(proporcao * tamanhoDaBarra) # faz o cálculo de multiplicação pra descobrir quantos caracteres serão preenchidos
    blocosVazios = tamanhoDaBarra - blocosPreenchidos

    barraPrenchida = "█" * blocosPreenchidos
    barraVazia = "░" * blocosVazios

    barra = barraPrenchida + barraVazia 

    if proporcao > 0.5:
        cor = VERDE
    elif proporcao > 0.2:
        cor = AMARELO
    else:
        cor = VERMELHO

    print(cor + barra + RESET)

# Função para exibir o HP dos personagens
def exibirLifePoints(jogador, adversario):
    print(f"{jogador["nome"]} | HP: {jogador["vidaAtual"]}")
    informacaoDaVidaDosPersonagens(jogador)
    print("\n")
    print(f"{adversario["nome"]} | HP: {adversario["vidaAtual"]}")
    informacaoDaVidaDosPersonagens(adversario)
    print("\n")

# Função para exibir as situações das rodadas
def exibicaoRodadas(titulo="RODADA", rodada = None):
    largura = 30 # controla a formatação das rodadas

    if rodada is not None:
        titulo = f"{titulo} {rodada}"

    print(f"""
{"=" * largura}
{titulo:^{largura}}
{"=" * largura}
""")

# Função para exibir o vencedor da batalha
def exibirVitoria(vencedor):
    largura = 30 # controla a formatação
    mensagem = f"{vencedor["nome"]} VENCEU!"

    print("=" * largura)
    print(f"{mensagem:^{largura}}")
    print("=" * largura)

# Função para exibir as habilidades do personagem
def exibirHabilidades(jogador):
    largura = 30 # controla a formatação

    print("HABILIDADES")
    print("-" * largura)
    for indice, golpe in enumerate(jogador["golpes"], start=1):
        print(f"{indice} - {golpe["nome"]} | Dano: {golpe["dano"]} | Cargas: {golpe["cargas"]}")
    
    print("-" * largura)