from front_end import FrontEnd
import joblib

def load_models():
    try:
        # Carrega os modelos
        models = {
            'knn': joblib.load('models/knn_model.joblib'),
            'mlp': joblib.load('models/mlp_model.joblib'),
            'dt': joblib.load('models/decision_tree_model.joblib'),
            'rf': joblib.load('models/random_forest_model.joblib'),
        }
    except FileNotFoundError:
        print("Error loading models. Exiting.")
        return None

    return models

def main():
    # Carrega os modelos
    models = load_models()
    if models is None:
        return 

    print("Welcome to Tic Tac Toe!")
    print("Choose a model to play with:")

    # Listar os modelos
    for idx, (model_name, model_data) in enumerate(models.items(), start=1):
        model_accuracy = model_data['accuracy']
        print(f"{idx}. {model_name} (Accuracy: {model_accuracy:.2f})")

    # Escolher o modelo
    choice = input("Enter the number of the model (1-4): ")
    try:
        chosen_model_name = list(models.keys())[int(choice) - 1]
        chosen_model = models[chosen_model_name]['model']
        print(f"You selected: {chosen_model_name}")
    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")
        return

    # Iniciar o jogo com o modelo escolhido
    front_end = FrontEnd(chosen_model)
    front_end.play_game()

if __name__ == "__main__":
    main()
