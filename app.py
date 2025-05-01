from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

# Sample Data - Steel Products (base price $1000/ton)
data = pd.DataFrame({
    'Base_Price': [1000, 1000, 1000, 1000, 1000, 800, 800, 1200, 1200, 1500],
    'Tariff_Percentage': [0, 10, 15, 20, 25, 10, 25, 10, 20, 15],
    'Price_Increase_Dollars': [0, 100, 150, 200, 250, 80, 200, 120, 240, 225]
})

# Train model
X = data[['Base_Price', 'Tariff_Percentage']]
y = data['Price_Increase_Dollars']
model = LinearRegression()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        base_price = float(request.form['base_price'])
        tariff_percent = float(request.form['tariff_percent'])
        
        # Predict price increase
        predicted_increase = model.predict([[base_price, tariff_percent]])[0]
        new_price = base_price + predicted_increase
        
        return render_template('index.html', 
                             base_price=base_price,
                             tariff_percent=tariff_percent,
                             price_increase=predicted_increase,
                             new_price=new_price)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
