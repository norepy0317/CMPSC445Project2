
'''
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load model
price_model = joblib.load('tariff_price_model.pkl')

@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.json
    x = np.array([[data['tariff_percent'], data['import_volume'], data['inflation_rate'], data['exchange_rate']]])
    predicted_price = price_model.predict(x)[0]
    return jsonify({'predicted_price': round(predicted_price, 2)})

@app.route('/predict_tariff', methods=['POST'])
def predict_tariff():
    # Re-create your model for tariff % (use your own saved model if needed)
    base_price = data['base_price']
    price_increase = data['price_increase_dollars']
    
    X = pd.DataFrame({
        'Base_Price': [base_price],
        'Price_Increase_Dollars': [price_increase]
    })
    
    model = LinearRegression()
    # You can train it here or load if saved
    model.fit(...)  # use your original logic here
    predicted_tariff = model.predict(X)[0]
    

    
    return jsonify({'predicted_tariff_percent': round(predicted_tariff, 2)})

if __name__ == '__main__':
    app.run(debug=True)
'''

# app.py

import os
from flask import Flask
import joblib
import numpy as np

app = Flask(__name__)

# Load pre-trained model
model = joblib.load('tariff_price_model.pkl')

@app.route('/')
def home():
    return "🟢 Tariff Price Predictor API is running!"

@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.json
    try:
        # Extract input features
        x_input = np.array([[
            float(data['tariff_percent']),
            float(data['import_volume']),
            float(data['inflation_rate']),
            float(data['exchange_rate'])
        ]])
        
        # Predict price
        predicted = model.predict(x_input)[0]
        return jsonify({
            'predicted_price': round(predicted, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  
    app.run(host='0.0.0.0', port=port, debug=True)
