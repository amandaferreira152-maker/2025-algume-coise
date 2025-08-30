import random

# Variáveis globais iniciais (valores iniciais)
vida1 = [100]
vida2 = [100]
congelado1 = [False]
congelado2 = [False]
jogador1 = ""
jogador2 = ""

def exibir_status():
    """
    Mostra o nome e a vida atual dos dois jogadores.
    """
    print(f"{jogador1}: {max(vida1[0], 0)}/100 HP")
    print(f"{jogador2}: {max(vida2[0], 0)}/100 HP")

def escolher_magia(nome):
    """
    Mostra o menu de magias e pede a escolha do jogador (1, 2 ou 3).
    Retorna a escolha.
    """
    while True:
        print(f"\n---------- Turno de {nome} -----------")
        print("Escolha sua magia: ")
        print("1. Bola de Fogo (Dano: 15-30)")
        print("2. Raio Congelante (Dano: 10-20, 25% chance de congelar)")
        print("3. Cura (Cura: 10-25)")
        escolha = input("Digite o número da magia (1, 2 ou 3): ")
        if escolha in ['1', '2', '3']:
            return int(escolha)
        else:
            print("Escolha inválida. Por favor, digite 1, 2 ou 3.")

def aplicar_bola_de_fogo(alvo):
    """
    Sorteia o dano entre 15 e 30 e aplica ao alvo.
    Retorna o novo valor de vida do alvo.
    """
    dano = random.randint(15, 30)
    alvo[0] -= dano
    print(f"Bola de Fogo! Causou {dano} de dano.")
    return alvo[0]

def aplicar_raio_congelante(alvo, alvo_congelado, nome_alvo):
    """
    Sorteia o dano entre 10 e 20 e aplica ao alvo.
    Sorteia chance de congelar (25% de chance).
    Se congelar, marca o alvo como congelado e informa ao jogador.
    Retorna o novo valor de vida do alvo.
    """
    dano = random.randint(10, 20)
    alvo[0] -= dano
    print(f"Raio Congelante! Causou {dano} de dano.")

    if random.random() < 0.25:
        alvo_congelado[0] = True
        print(f"{nome_alvo} foi congelado!")
    return alvo[0]

def aplicar_cura(jogador_vida):
    """
    Sorteia o valor da cura entre 10 e 25.
    Soma na vida do jogador (não pode passar de 100).
    Mostra quanto foi recuperado.
    Retorna o novo valor de vida do jogador.
    """
    cura = random.randint(10, 25)
    vida_antes = jogador_vida[0]
    jogador_vida[0] = min(100, jogador_vida[0] + cura)
    recuperado = jogador_vida[0] - vida_antes
    print(f"Cura! Recuperou {recuperado} de vida.")
    return jogador_vida[0]

def turno(nome_jogador, jogador_vida, jogador_congelado, alvo_vida, alvo_congelado, nome_alvo):
    """
    Gerencia o turno de um jogador.
    Verifica se o jogador está congelado, e se sim, remove o congelamento.
    Caso contrário, pede a escolha da magia e a executa.
    """
    if jogador_congelado[0]:
        print(f"{nome_jogador} está congelado e perdeu o turno!")
        jogador_congelado[0] = False
        return

    escolha = escolher_magia(nome_jogador)

    if escolha == 1:
        aplicar_bola_de_fogo(alvo_vida)
    elif escolha == 2:
        aplicar_raio_congelante(alvo_vida, alvo_congelado, nome_alvo)
    elif escolha == 3:
        aplicar_cura(jogador_vida)

# Programa Principal
print("=== Batalha de Magos ===")
jogador1 = input("Digite o nome do Jogador 1: ")
jogador2 = input("Digite o nome do Jogador 2: ")

turno_num = 1

# Enquanto os dois jogadores estiverem vivos:
while vida1[0] > 0 and vida2[0] > 0:
    print(f"\n===== TURNO {turno_num} =====")
    
    # Mostra o status
    exibir_status()

    # Turno do Jogador 1
    turno(jogador1, vida1, congelado1, vida2, congelado2, jogador2)

    # Verifica se o Jogador 2 ainda está vivo antes de seu turno
    if vida2[0] <= 0:
        break

    # Turno do Jogador 2
    turno(jogador2, vida2, congelado2, vida1, congelado1, jogador1)

    turno_num += 1

# Após o jogo terminar:
print("\n===== FIM DE JOGO =====")
exibir_status()

if vida1[0] > 0:
    print(f"Parabéns, {jogador1} venceu a batalha!")
else:
    print(f"Parabéns, {jogador2} venceu a batalha!")
