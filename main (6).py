# ==========================================
# 🎮 JOGO DA VELHA VS IA
# 🤖 Com Sistema de Pontuação
# Autor: Vinícius Knabben
# ==========================================

import random

# -----------------------------
# Variáveis Globais
# -----------------------------
placar = {"Jogador": 0, "IA": 0, "Empates": 0}

# -----------------------------
# Mostrar tabuleiro
# -----------------------------
def mostrar_tabuleiro(tabuleiro):
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

# -----------------------------
# Verificar vitória
# -----------------------------
def verificar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for c in combinacoes:
        if tabuleiro[c[0]] == jogador and tabuleiro[c[1]] == jogador and tabuleiro[c[2]] == jogador:
            return True
    return False

# -----------------------------
# Verificar empate
# -----------------------------
def verificar_empate(tabuleiro):
    return " " not in tabuleiro

# -----------------------------
# Movimento da IA
# -----------------------------
def movimento_ia(tabuleiro):
    
    # 1️⃣ Tenta ganhar
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "O"
            if verificar_vitoria(tabuleiro, "O"):
                return
            tabuleiro[i] = " "
    
    # 2️⃣ Bloqueia jogador
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "X"
            if verificar_vitoria(tabuleiro, "X"):
                tabuleiro[i] = "O"
                return
            tabuleiro[i] = " "
    
    # 3️⃣ Escolhe posição aleatória
    livres = [i for i in range(9) if tabuleiro[i] == " "]
    escolha = random.choice(livres)
    tabuleiro[escolha] = "O"

# -----------------------------
# Jogo principal
# -----------------------------
def jogar():
    
    tabuleiro = [" " for _ in range(9)]
    
    while True:
        mostrar_tabuleiro(tabuleiro)
        
        # Jogador
        try:
            pos = int(input("Sua jogada (1-9): ")) - 1
            
            if pos < 0 or pos > 8 or tabuleiro[pos] != " ":
                print("⚠ Jogada inválida!")
                continue
            
            tabuleiro[pos] = "X"
            
            if verificar_vitoria(tabuleiro, "X"):
                mostrar_tabuleiro(tabuleiro)
                print("🎉 Você venceu!")
                placar["Jogador"] += 1
                break
            
            if verificar_empate(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                print("🤝 Empate!")
                placar["Empates"] += 1
                break
            
            # IA joga
            movimento_ia(tabuleiro)
            
            if verificar_vitoria(tabuleiro, "O"):
                mostrar_tabuleiro(tabuleiro)
                print("🤖 IA venceu!")
                placar["IA"] += 1
                break
            
            if verificar_empate(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                print("🤝 Empate!")
                placar["Empates"] += 1
                break
        
        except ValueError:
            print("⚠ Digite apenas números!")

# -----------------------------
# Loop geral
# -----------------------------
if __name__ == "__main__":
    
    while True:
        print("===================================")
        print("        🎮 JOGO DA VELHA VS IA")
        print("===================================")
        print(f"🏆 Placar: Você {placar['Jogador']} | IA {placar['IA']} | Empates {placar['Empates']}")
        print("-----------------------------------")
        
        print("Posições:")
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 ")
        
        jogar()
        
        continuar = input("\nDeseja jogar novamente? (s/n): ").lower()
        if continuar != "s":
            print("\n👋 Obrigado por jogar!")
            break