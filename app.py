from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Charger le modèle, le scaler et les noms des caractéristiques
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')
feature_names = joblib.load('feature_names.joblib')


def preprocess_input(data):
    # Convertir les valeurs numériques en float au cas où elles seraient des chaînes de caractères
    numeric_features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
    for feature in numeric_features:
        if feature in data:
            try:
                data[feature] = float(data[feature])
            except ValueError:
                data[feature] = 0  # ou une autre valeur par défaut

    # Convertir les valeurs booléennes
    bool_features = ['mainroad', 'guestroom', 'basement',
                     'hotwaterheating', 'airconditioning', 'prefarea']
    for feature in bool_features:
        if feature in data:
            try:
                data[feature] = 1 if data[feature].lower() == 'yes' else 0
            except AttributeError:
                data[feature] = 0

    return data


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
    except:
        return jsonify({'error': 'Invalid input format. Please send a JSON object.'}), 400

    data = preprocess_input(data)

    input_df = pd.DataFrame([data])

    # Encoder les variables catégorielles
    categorical_features = ['furnishingstatus']
    input_df = pd.get_dummies(
        input_df, columns=categorical_features, drop_first=True)

    # S'assurer que toutes les colonnes nécessaires sont présentes sinon les ajouter avec des valeurs par défaut à 0
    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0

    # Réorganiser les colonnes
    input_df = input_df.reindex(columns=feature_names, fill_value=0)
    # Normaliser les caractéristiques numériques
    numeric_features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
    input_df[numeric_features] = scaler.transform(input_df[numeric_features])

    # Faire la prédiction
    prediction = model.predict(input_df)

    return jsonify({'predicted_price': float(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True)
