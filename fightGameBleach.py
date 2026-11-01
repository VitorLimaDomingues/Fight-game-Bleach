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

# Criando os personagens através da função criarPersonagem
ichigo = criarPersonagem("Ichigo Kurosaki", 100, 5, 20, ichigoHabilidades)
ulquiorra = criarPersonagem("Ulquiorra Ciffer", 100, 7, 18, ulquiorraHabilidades)

print(ichigo)
print(ulquiorra)

# Função para escolha de personagem
def escolher(personagens):
    for indice, personagem in enumerate(personagens, start=1):
        print(f"{indice} - {personagem['nome']}")

    while True:
        try: 
            escolha = int(input("Escolha um personagem: "))

            if 1 <= escolha <= len(personagens):
                return personagens[escolha - 1]
            else:
                print("Personagem inexistente! Tente novamente.")


        except ValueError:
            print("Digite apenas números!")

personagens = [ichigo, ulquiorra]
personagemEscolhido = escolher(personagens)