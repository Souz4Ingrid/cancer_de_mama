import numpy as np
from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

# Carregamento seguro do Modelo e seus artefatos
model_path = 'modelo_cancer_mama.pkl'
loaded_data = None

if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        loaded_data = pickle.load(f)
    print("Sistema de IA carregado com sucesso!")
else:
    print("ERRO: Execute 'treinamento.py' primeiro para gerar o arquivo de modelo.")

@app.route('/')
def home():
    if loaded_data:
        # Usa os nomes das colunas salvos no treinamento para gerar o formulário
        feature_names = loaded_data['features']
        return render_template('index.html', feature_names=feature_names)
    else:
        return "Erro: Modelo não encontrado. Execute o script de treinamento."

@app.route('/predict', methods=['POST'])
def predict():
    if not loaded_data:
        return "Erro interno: Modelo de IA não disponível.", 500

    try:
        # Recupera as ferramentas do pacote
        model = loaded_data['model']
        scaler = loaded_data['scaler']
        feature_names = loaded_data['features']
        class_names = loaded_data['classes'] # Ex: ['B', 'M']

        # Coleta os dados do formulário na ordem correta
        form_data = request.form.to_dict()
        input_features = []
        
        for name in feature_names:
            val = form_data.get(name)
            if val is None:
                raise ValueError(f"Campo faltando: {name}")
            input_features.append(float(val))
        
        # Transforma a lista num array 2D
        features_array = np.array([input_features])
        
        # IMPORTANTE: Aplica a mesma escala usada no treino!
        features_scaled = scaler.transform(features_array)
        
        # Previsão
        prediction_index = model.predict(features_scaled)[0]
        prediction_label = class_names[prediction_index]
        
        # Tradução amigável para o usuário
        if prediction_label == 'M':
            resultado_extenso = "MALIGNO"
        elif prediction_label == 'B':
            resultado_extenso = "BENIGNO"
        else:
            resultado_extenso = prediction_label

        result_message = f'O modelo previu que o tumor é: {resultado_extenso}'
        
    except ValueError as ve:
        result_message = f'Erro de Preenchimento: {str(ve)}'
    except Exception as e:
        result_message = f'Erro inesperado: {e}'

    # Renderiza novamente a página com o resultado
    feature_names = loaded_data['features']
    return render_template('index.html', prediction_text=result_message, feature_names=feature_names)

if __name__ == "__main__":
    app.run(debug=True)