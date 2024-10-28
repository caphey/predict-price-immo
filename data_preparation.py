import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Charger les données
data = pd.read_csv('Housing.csv')

# Sélectionner les caractéristiques et la cible
features = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement',
            'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']
target = 'price'

X = data[features]  # X contient les caractéristiques
y = data[target]    # y contient la variable cible (prix)

# Encoder les variables catégorielles en variables binaires
X = pd.get_dummies(X, columns=['mainroad', 'guestroom', 'basement',
                   'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus'], drop_first=True)

# Convertir les colonnes booléennes en entiers
bool_columns = X.select_dtypes(include=['bool']).columns
X[bool_columns] = X[bool_columns].astype(int)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Normaliser les caractéristiques numériques
scaler = StandardScaler()
numeric_features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
X_train[numeric_features] = scaler.fit_transform(X_train[numeric_features])
X_test[numeric_features] = scaler.transform(X_test[numeric_features])

# Sauvegarder le scaler et les noms des colonnes
joblib.dump(scaler, 'scaler.joblib')
joblib.dump(X_train.columns.tolist(), 'feature_names.joblib')

print("Données chargées et préparées avec succès!")
print(f"Nombre d'échantillons d'entraînement : {X_train.shape[0]}")
print(f"Nombre d'échantillons de test : {X_test.shape[0]}")
print(f"Nombre de caractéristiques : {X_train.shape[1]}")

# Afficher les premières lignes des données préparées
print("\nAperçu des données préparées:")
print(X_train.head())

# Ne pas oublier d'exporter ces variables pour qu'elles soient accessibles dans train_model.py
if __name__ == '__main__':
    print("Ce script a été exécuté directement.")
else:
    print("Ce script a été importé comme un module.")
