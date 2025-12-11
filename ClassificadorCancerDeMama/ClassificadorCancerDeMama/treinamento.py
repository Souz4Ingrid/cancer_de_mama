import pandas as pd
import pickle
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_and_save():
    # 1. Configuração de Caminhos
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Vamos salvar o modelo na mesma pasta para facilitar a leitura pelo app.py
    output_path = os.path.join(current_dir, "modelo_cancer_mama.pkl")
    csv_path = os.path.join(current_dir, "data.csv")

    if not os.path.exists(csv_path):
        print(f"ERRO: Arquivo 'data.csv' não encontrado em: {csv_path}")
        return

    # 2. Carregamento e Limpeza
    df = pd.read_csv(csv_path)
    
    if 'id' in df.columns:
        df = df.drop('id', axis=1)
    if 'Unnamed: 32' in df.columns: # Remove coluna de erro comum nesse dataset
        df = df.drop('Unnamed: 32', axis=1)
        
    df = df.dropna(axis=1, how='all')

    # 3. Separação X e y
    y_raw = df['diagnosis']
    X = df.drop('diagnosis', axis=1)
    
    # Guardamos os nomes das colunas para usar no front-end
    feature_names = X.columns.tolist()

    # 4. Codificação do Alvo (M/B -> 1/0)
    le = LabelEncoder()
    y = le.fit_transform(y_raw) # Geralmente: B=0, M=1

    # 5. Divisão Treino/Teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 6. Escalonamento (A Régua)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 7. Treinamento do Modelo
    model = DecisionTreeClassifier(
        max_depth=5,
        min_samples_split=10,
        min_samples_leaf=5,
        random_state=42
    )
    model.fit(X_train, y_train)

    # 8. Avaliação Rápida
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"Acurácia do modelo: {acc:.2f}")

    # 9. Salvando o Pacote Completo (Cérebro + Régua + Informações)
    dataset_package = {
        "model": model,
        "scaler": scaler,           # Essencial para o app.py
        "classes": le.classes_,     # ['B', 'M']
        "features": feature_names   # Nomes das colunas
    }

    with open(output_path, "wb") as f:
        pickle.dump(dataset_package, f)
        
    print(f"Sucesso! Arquivo gerado: {output_path}")

if __name__ == "__main__":
    train_and_save()