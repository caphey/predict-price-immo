# Projet de Prédiction de Prix Immobilier

Ce projet utilise un modèle de régression linéaire pour prédire les prix des biens immobiliers en fonction de diverses caractéristiques. Il comprend une application frontend en React et un backend en Flask.

## Installation

### Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3.6 ou supérieur
- Node.js et npm
- Git

### Cloner le dépôt

Clonez le dépôt Git sur votre machine locale :

```sh
git clone https://github.com/caphey/price-immo.git
cd price-immo
```

## Lancer le Projet

Pour lancer le projet, suivez les étapes ci-dessous :

### Backend

1. Installez les dépendances

2. Lancez le serveur Flask :
   ```sh
   python app.py
   ```

### Frontend

1. Naviguez dans le répertoire `frontend` :

   ```sh
   cd frontend
   ```

2. Installez les dépendances :

   ```sh
   npm install
   ```

3. Lancez l'application React :
   ```sh
   npm run dev
   ```

## Utilisation

### Préparation des Données

Le fichier [data_preparation.py](data_preparation.py) contient le code pour préparer les données d'entraînement et de test.

### Entraînement du Modèle

Le fichier [train_model.py](train_model.py) entraîne le modèle de régression linéaire et le sauvegarde dans `model.joblib`.

### Prédiction

Le fichier [app.py](app.py) contient le code pour le serveur Flask qui reçoit les données de l'utilisateur, les prétraite, et renvoie une prédiction de prix.

### Interface Utilisateur

Le frontend est développé en React et se trouve dans le répertoire [frontend](frontend). Le composant principal est [App.jsx](frontend/src/App.jsx) et le formulaire de prédiction est dans [PredictionForm.jsx](frontend/src/components/PredictionForm.jsx).

## API

### Endpoint `/predict`

- **Méthode**: POST
- **Description**: Prend un JSON avec les caractéristiques du bien immobilier et renvoie le prix prédit.
- **Exemple de requête**:
  ```json
  {
    "area": 5000,
    "bedrooms": 3,
    "bathrooms": 2,
    "stories": 2,
    "mainroad": "yes",
    "guestroom": "no",
    "basement": "no",
    "hotwaterheating": "no",
    "airconditioning": "yes",
    "parking": 1,
    "prefarea": "yes",
    "furnishingstatus": "furnished"
  }
  ```
- **Exemple de réponse**:
  ```json
  {
    "predicted_price": 7500000.0
  }
  ```
