# Jogo de luta inspirado no anime Bleach

# Função para criação dos personagens

def criarPersonagem(nome, vida, ataque, defesa):
    personagem = {
        "nome": nome,
        "vida": vida,
        "ataque": ataque,
        "defesa": defesa
    }

    return personagem

ichigo = criarPersonagem("Ichigo Kurosaki", 100, 5, 20)

print(ichigo)