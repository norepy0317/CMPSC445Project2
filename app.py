
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
'''
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
'''
'''
from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model = joblib.load('tariff_price_model.pkl')

# Define the prediction route
@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.get_json()  # Get the input data from the POST request

    # Extract the relevant input values from the request
    tariff_percent = data['tariff_percent']
    import_volume = data['import_volume']
    inflation_rate = data['inflation_rate']
    exchange_rate = data['exchange_rate']

    # Convert the input values into a numpy array for prediction
    input_data = np.array([[tariff_percent, import_volume, inflation_rate, exchange_rate]])

    # Predict the product price using the model
    predicted_price = model.predict(input_data)[0]

    # Return the prediction as a JSON response
    return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Ensure it binds to the port Render provides
    app.run(host='0.0.0.0', port=port, debug=True)
'''

from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS


# Initialize Flask app
app = Flask(__name__)
CORS(app)  # This line enables CORS for all routes


# Load your trained model (make sure the .pkl file is in the same directory or provide the correct path)
model = joblib.load('tariff_price_model.pkl')

@app.route('/')
def index():
    return '🟢 Tariff Price Predictor API is running!'

# This route handles the POST request at /predict_price
@app.route('/predict_price', methods=['POST'])
def predict_price():
    try:
        # Get the input data from the POST request
        data = request.get_json()

        # Extract values from the request data
        tariff_percent = data.get('tariff_percent')
        import_volume = data.get('import_volume')
        inflation_rate = data.get('inflation_rate')
        exchange_rate = data.get('exchange_rate')

        # Prepare the input data for prediction
        input_data = np.array([[tariff_percent, import_volume, inflation_rate, exchange_rate]])

        # Make the prediction using the model
        predicted_price = model.predict(input_data)[0]

        # Return the predicted price as JSON
        return jsonify({'predicted_price': predicted_price})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the app (Render will handle the port binding automatically)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
