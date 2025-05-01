from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

# Initialize model (same as before)
data = pd.DataFrame({
    'Base_Price': [1000, 1000, 1000, 1000, 1000, 800, 800, 1200, 1200, 1500],
    'Tariff_Percentage': [0, 10, 15, 20, 25, 10, 25, 10, 20, 15],
    'Price_Increase_Dollars': [0, 100, 150, 200, 250, 80, 200, 120, 240, 225]
})

X = data[['Base_Price', 'Tariff_Percentage']]
y = data['Price_Increase_Dollars']
model = LinearRegression()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            base_price = float(request.form['base_price'])
            tariff_percent = float(request.form['tariff_percent'])
            predicted_increase = model.predict([[base_price, tariff_percent]])[0]
            new_price = base_price + predicted_increase
            return render_template(
                'index.html',
                result=True,
                base_price=f"{base_price:,.2f}",
                tariff_percent=f"{tariff_percent:.1f}",
                price_increase=f"{predicted_increase:,.2f}",
                new_price=f"{new_price:,.2f}"
            )
        except:
            return render_template('index.html', error=True)
    
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
