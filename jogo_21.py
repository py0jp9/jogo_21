import random

# ========================
# CONFIGURAÇÃO DO BARALHO
# ========================

def criar_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = [f'{v}{n}' for n in naipes for v in valores]
    random.shuffle(baralho)
    return baralho


def pegar_valor(carta):
    valor = carta[:-1]  
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    else:
        return int(valor)


def calcular_pontos(mao):
    total = 0
    ases = 0

    for carta in mao:
        if carta[:-1] == 'A':
            ases += 1
            total += 11
        else:
            total += pegar_valor(carta)

    # Se passou de 21 e tem Ás, transforma 11 em 1
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1

    return total


# ========================
# EXIBIÇÃO
# ========================

def exibir_mao(nome, mao, esconder_segunda=False):
    if esconder_segunda:
        print(f"{nome}: {mao[0]} [?]")
    else:
        pontos = calcular_pontos(mao)
        print(f"{nome}: {' '.join(mao)} → {pontos} pontos")


# ========================
# LÓGICA DO JOGO
# ========================

def vez_do_dealer(baralho, mao_dealer):
    print("\n--- Vez do Dealer ---")
    while calcular_pontos(mao_dealer) < 17:
        mao_dealer.append(baralho.pop())
        print(f"Dealer comprou uma carta...")
    exibir_mao("Dealer", mao_dealer)


def verificar_vencedor(mao_jogador, mao_dealer):
    pontos_jogador = calcular_pontos(mao_jogador)
    pontos_dealer = calcular_pontos(mao_dealer)

    print("\n=============================")
    print(f"Você: {pontos_jogador} pontos")
    print(f"Dealer: {pontos_dealer} pontos")
    print("=============================")

    if pontos_jogador > 21:
        print("❌ Você passou de 21! Dealer vence.")
    elif pontos_dealer > 21:
        print("✅ Dealer passou de 21! Você vence!")
    elif pontos_jogador > pontos_dealer:
        print("✅ Você vence!")
    elif pontos_jogador < pontos_dealer:
        print("❌ Dealer vence.")
    else:
        print("🤝 Empate!")


# ========================
# LOOP PRINCIPAL
# ========================

def jogar():
    print("=" * 35)
    print("       BEM-VINDO AO BLACKJACK!")
    print("=" * 35)

    while True:
        baralho = criar_baralho()

        mao_jogador = [baralho.pop(), baralho.pop()]
        mao_dealer  = [baralho.pop(), baralho.pop()]

        print("\n--- Cartas iniciais ---")
        exibir_mao("Você", mao_jogador)
        exibir_mao("Dealer", mao_dealer, esconder_segunda=True)

        if calcular_pontos(mao_jogador) == 21:
            print("\n🎉 BLACKJACK! Você vence na primeira mão!")
            exibir_mao("Dealer", mao_dealer)
        else:
            while True:
                print(f"\nSua mão: {' '.join(mao_jogador)} → {calcular_pontos(mao_jogador)} pontos")
                escolha = input("O que deseja fazer? [P]edir carta / [S]top: ").strip().upper()

                if escolha == 'P':
                    mao_jogador.append(baralho.pop())
                    if calcular_pontos(mao_jogador) > 21:
                        exibir_mao("Você", mao_jogador)
                        print("❌ Você passou de 21! Dealer vence.")
                        break
                elif escolha == 'S':
                    vez_do_dealer(baralho, mao_dealer)
                    verificar_vencedor(mao_jogador, mao_dealer)
                    break
                else:
                    print("Opção inválida. Digite P ou S.")

        print()
        jogar_novamente = input("Deseja jogar novamente? [S]im / [N]ão: ").strip().upper()
        if jogar_novamente != 'S':
            print("\nObrigado por jogar! Até mais 👋")
            break


# ========================
# INICIAR
# ========================

if __name__ == "__main__":
    jogar()