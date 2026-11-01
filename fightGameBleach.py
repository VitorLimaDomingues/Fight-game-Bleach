# Jogo de luta inspirado no anime Bleach

# Função para criação dos personagens

def criarPersonagem(nome, vida, ataque, defesa, golpes):
    personagem = {
        "nome": nome,
        "vida": vida,
        "ataque": ataque,
        "defesa": defesa,
        "golpes": golpes
    }

    return personagem

# Golpes e Transformações

ichigoHabilidades = [
    {"nome": "Getsuga Tenshou", "dano": 30},
    {"nome": "Estocada", "dano": 12},
    ]
    
ulquiorraHabilidades = [
    {"nome": "Estocada", "dano": 10},
    {"nome": "Cero", "dano": 20}
]

ichigo = criarPersonagem("Ichigo Kurosaki", 100, 5, 20, ichigoHabilidades)
ulquiorra = criarPersonagem("Ulquiorra Ciffer", 100, 7, 18, ulquiorraHabilidades)

print(ichigo)
print(ulquiorra)