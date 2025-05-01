# train_tariff_model.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# Optional: For EDA/Debugging only
import seaborn as sns
import matplotlib.pyplot as plt

# === STEP 1: Create synthetic dataset ===
np.random.seed(0)
n = 200
data = pd.DataFrame({
    'tariff_percent': np.random.uniform(0, 20, n),
    'import_volume': np.random.uniform(1000, 10000, n),
    'inflation_rate': np.random.uniform(1, 5, n),
    'exchange_rate': np.random.uniform(0.8, 1.2, n),
    'product_price': np.random.uniform(10, 100, n)
})

# Simulate economic impact
data['product_price'] += 0.5 * data['tariff_percent'] + 0.3 * data['inflation_rate']

# === STEP 2: Train model ===
X = data[['tariff_percent', 'import_volume', 'inflation_rate', 'exchange_rate']]
y = data['product_price']

model = RandomForestRegressor()
model.fit(X, y)

# === STEP 3: Save model for web use ===
joblib.dump(model, 'tariff_price_model.pkl')
print("✅ Model saved as 'tariff_price_model.pkl'")

# === OPTIONAL: Visualization for dev/debug ===
if __name__ == "__main__":
    sns.pairplot(data)
    plt.suptitle("Pairwise Feature Relationships", y=1.02)
    plt.show()
