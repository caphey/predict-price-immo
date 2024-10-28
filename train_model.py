from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import joblib
import pandas as pd
from data_preparation import X_train, X_test, y_train, y_test

# Créer et entraîner le modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluer le modèle
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Erreur quadratique moyenne (MSE): {mse}")
print(f"Racine de l'erreur quadratique moyenne (RMSE): {rmse}")
print(f"Coefficient de détermination (R²): {r2}")

# Sauvegarder le modèle pour une utilisation ultérieure
joblib.dump(model, 'model.joblib')
print("\nModèle sauvegardé avec succès!")

# Exemple de prédiction
sample = X_test.iloc[0]  # Prenons le premier exemple de l'ensemble de test
prediction = model.predict([sample])
print(f"\nPrédiction pour l'exemple: {prediction[0]}")
print(f"Valeur réelle: {y_test.iloc[0]}")

# Afficher les caractéristiques de l'exemple
print("\nCaractéristiques de l'exemple:")
for feature, value in sample.items():
    print(f"{feature}: {value}")
