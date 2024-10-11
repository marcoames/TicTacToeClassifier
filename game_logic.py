import random

class GameLogic:
    def __init__(self):
        # Cria o tabuleiro vazio
        self.board = [0] * 9

    def print_board(self):
        symbols = {2: 'X', 1: 'O', 0: ' '}
        display_board = [symbols[cell] for cell in self.board]

        print("\n")
        print(f"{display_board[0]} | {display_board[1]} | {display_board[2]}")
        print("--+---+--")
        print(f"{display_board[3]} | {display_board[4]} | {display_board[5]}")
        print("--+---+--")
        print(f"{display_board[6]} | {display_board[7]} | {display_board[8]}")
        print("\n")

    def user_move(self):
        # O usuário escolhe uma posição
        while True:
            try:
                move = int(input("Escolha sua posição (1-9): ")) - 1
                if self.board[move] == 0:
                    self.board[move] = 2
                    break
                else:
                    print("Posição já ocupada. Escolha outra.")
            except (IndexError, ValueError):
                print("Entrada inválida. Escolha um número de 1 a 9.")

    def computer_move(self):
        # Computador escolhe uma jogada aleatória nas posições vazias
        available_moves = [i for i, cell in enumerate(self.board) if cell == 0]
        move = random.choice(available_moves)
        self.board[move] = 1
        print(f"\nComputador joga na posição {move + 1}")

    def check_winner(self):
        # Verifica todas as combinações de vitória

        winning_combinations = [
            [0, 1, 2],  # Linha 1
            [3, 4, 5],  # Linha 2
            [6, 7, 8],  # Linha 3
            [0, 3, 6],  # Coluna 1
            [1, 4, 7],  # Coluna 2
            [2, 5, 8],  # Coluna 3
            [0, 4, 8],  # Diagonal principal
            [2, 4, 6],  # Diagonal secundária
        ]

        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != 0:
                return 'Xganha' if self.board[combination[0]] == 2 else 'Oganha'

        # Verifica se há empate
        if all(cell != 0 for cell in self.board):
            return 'Empate'

        return 'Temjogo'  # Jogo ainda em andamento
