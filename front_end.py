from game_logic import GameLogic

class FrontEnd:
    def __init__(self, model):
        self.game = GameLogic()
        self.model = model
        self.acertos = 0  # Contador de acertos
        self.erros = 0    # Contador de erros

    def play_game(self):
        game_over = False

        while not game_over:
            # Usuário joga
            self.game.print_board()
            self.game.user_move()

            # IA classifica
            prediction = self.get_prediction()
            print(f"IA classifica o estado como: {prediction}")

            # Verifica se o jogo acabou pela previsão
            if self.check_game_over(prediction):
                game_over = True
                break
            
            # Imprimir resultados
            print(f"Acertos: {self.acertos}, Erros: {self.erros}")

            # Computador joga
            self.game.computer_move()

            # IA classifica
            prediction = self.get_prediction()
            print(f"IA classifica o estado como: {prediction}")

            # Verifica se o jogo acabou pela previsão
            if self.check_game_over(prediction):
                game_over = True
                break
            # Imprimir resultados
            print(f"Acertos: {self.acertos}, Erros: {self.erros}")

        # Imprimir resultados
        print(f"Acertos: {self.acertos}, Erros: {self.erros}")

    # Predição da IA
    def get_prediction(self):
        # Predição com o board
        prediction = self.model.predict([self.game.board])[0]
        
        if prediction == 1:
            return 'Xganha'
        elif prediction == 2:
            return 'Oganha'
        elif prediction == 3:
            return 'Temjogo'
        else:
            return 'Empate'

    # Verifica se o jogo acabou
    def check_game_over(self, prediction):
        resultado_real = self.game.check_winner()  # retorna o resultado real do jogo

        if resultado_real == 'Xganha' and prediction == 'Xganha':
            self.acertos += 1
        elif resultado_real == 'Oganha' and prediction == 'Oganha':
            self.acertos += 1
        elif resultado_real == 'Empate' and prediction == 'Empate':
            self.acertos += 1
        elif resultado_real == 'Temjogo' and prediction == 'Temjogo':
            self.acertos += 1
        else:
            self.erros += 1

        if resultado_real != 'Temjogo':
            self.game.print_board()
            print(f"Resultado real do jogo: {resultado_real}")
            return True  # Jogo acabou
        return False  # Jogo continua
