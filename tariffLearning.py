import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import seaborn as sns
import matplotlib.pyplot as plt


# Create synthetic dataset
np.random.seed(0)
n = 200
data = pd.DataFrame({
    'tariff_percent': np.random.uniform(0, 20, n),
    'import_volume': np.random.uniform(1000, 10000, n),
    'inflation_rate': np.random.uniform(1, 5, n),
    'exchange_rate': np.random.uniform(0.8, 1.2, n),
    'product_price': np.random.uniform(10, 100, n)
})
data['product_price'] += 0.5 * data['tariff_percent'] + 0.3 * data['inflation_rate']

# Train model
X = data[['tariff_percent', 'import_volume', 'inflation_rate', 'exchange_rate']]
y = data['product_price']
model = RandomForestRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, 'tariff_price_model.pkl')


sns.pairplot(data)
plt.suptitle("Pairwise Feature Relationships", y=1.02)
plt.show()

# Scenario: Chinese goods with 125% tariff
tariff = 125.0
import_vol = 5000
inflation = 3.0
exchange = 1.0

# Predict price
input_data = np.array([[tariff, import_vol, inflation, exchange]])
predicted_price = model.predict(input_data)[0]

print(f"📦 Predicted price of Chinese import with 125% tariff: ${predicted_price:.2f}")

tariff_range = np.linspace(0, 30, 100)
prices = []

for t in tariff_range:
    x = np.array([[t, import_vol, inflation, exchange]])
    p = model.predict(x)[0]
    prices.append(p)

plt.figure(figsize=(10, 5))
plt.plot(tariff_range, prices, color='orange')
plt.title("Effect of Tariff % on Predicted Product Price")
plt.xlabel("Tariff (%)")
plt.ylabel("Predicted Price ($)")
plt.grid(True)
plt.show()

