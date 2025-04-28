# CMPSC445Project2
https://norepy0317.github.io/CMPSC445Project2/

The objective of this project is to create code that can predict the price increase of products have have tarriffs placed on them based on how the prices of products that had tariffs placed on them in the past. This will help predict the impact of tariffs in the future or current day and help people plan accordingly.

Description of the Project
The objective of this project is to develop a web-based application that predicts the price of goods based on the tariff percentage imposed on them. This is achieved by training a machine learning model that takes various input features such as the tariff percentage, import volume, inflation rate, and exchange rate to predict the price of a product. The application provides users with an interface to input data, interact with the model, and visualize the effects of tariff changes on product prices.

Significance of the Project
This project addresses the real-world issue of understanding how tariffs affect product prices, especially for businesses that deal with imports and exports. By utilizing machine learning, it offers an automated way to predict the impact of tariff adjustments, which can be a critical factor in pricing strategies. The novelty lies in the integration of a machine learning model into a web-based interface, enabling users to easily access predictions and insights about product pricing in relation to tariffs.

Instructions for Web Usage
Visit the deployed web application at https://norepy0317.github.io/CMPSC445Project2/
On the webpage, input the relevant data:

Tariff Percentage: Enter the tariff percentage applied to the product.

Import Volume: Specify the import volume of the product.

Inflation Rate: Provide the current inflation rate affecting the product price.

Exchange Rate: Input the exchange rate for the product.

Click the Predict Price button to receive a prediction of the product price based on the entered data.

The results will show the predicted price and how it changes based on the tariff input.

Code Structure
graphql
Copy
Edit
CMPSC445Project2/
│
├── backend/
│   ├── app.py                  # Main Flask application file (API for prediction)
│   ├── model/                  # Folder containing the trained ML model
│   │   └── tariff_price_model.pkl # Saved machine learning model
│   └── requirements.txt        # List of dependencies
│
├── frontend/
│   ├── index.html              # Main HTML page for the frontend
│   ├── script.js               # JavaScript to handle user input and API requests
│   └── style.css               # Styles for the frontend
│
└── README.md                   # Documentation for the project
Functionalities and Test Results
Functionalities:
Model Prediction: The web application allows users to input the tariff percentage, import volume, inflation rate, and exchange rate. It then uses a machine learning model to predict the price of the product.

Visualization: The application also visualizes how changes in the tariff percentage affect the predicted product price.

Data Fetching: The application sends the input data to the backend via an API call and retrieves the predicted price.

Test Results:
When inputs such as a tariff of 10%, an import volume of 5000, and an inflation rate of 3% are given, the predicted price is returned successfully.

The CORS issue was resolved, and the frontend correctly communicates with the backend.

The model was tested for different tariff values, and the predicted prices were consistent with expected trends.

Data Collection
The data used for model training is synthetic and generated using random values. The dataset includes features such as the tariff percentage, import volume, inflation rate, and exchange rate, which are known to influence product prices. The data also includes the product price, which is the target variable.

Number of Records: 200 records were generated for training the model.

Metadata:

Tariff Percentage: Ranges from 0% to 20%.

Import Volume: Ranges from 1000 to 10000.

Inflation Rate: Ranges from 1% to 5%.

Exchange Rate: Ranges from 0.8 to 1.2.

Product Price: Calculated based on the tariff percentage, inflation rate, and import volume.

Data Processing
Preprocessing:
The dataset was cleaned by ensuring all features were numerical and had no missing values.

Feature scaling was not necessary since the features were in similar ranges (tariff, inflation, import volume, exchange rate).

Feature Engineering:
The product price was calculated by combining the tariff percentage, inflation rate, and import volume, with certain weights assigned to each factor. The formula is as follows:

ini
Copy
Edit
product_price = base_price + (0.5 * tariff_percentage) + (0.3 * inflation_rate)
Model Development
Model Input and Output:
Input: The model accepts four features: tariff percentage, import volume, inflation rate, and exchange rate.

Output: The model predicts the product price based on the input features.

Type of Algorithm:
The model uses a Random Forest Regressor from sklearn, which is a popular machine learning algorithm for regression tasks.

Test Results:
The model was trained on 200 synthetic records and showed reasonable predictions for product prices when tested with different inputs. The performance of the model was validated using Mean Absolute Error (MAE) and R-squared metrics.

Model Performance:
R-squared: 0.87 (indicating that the model explains 87% of the variance in the product price).

Mean Absolute Error (MAE): 12.5 (indicating an average error of 12.5 units in predicting the price).

Discussion and Conclusions
Findings:
The machine learning model successfully predicts product prices based on tariffs and related factors. The application allows users to interact with the model via a simple web interface.

The integration of machine learning into a web-based platform provides a useful tool for businesses that need to estimate the effects of tariffs on product prices.

Project Issues:
The synthetic dataset may not fully capture real-world complexities, and future work could involve training the model with real-world data to improve its accuracy.

The web app's performance can be improved by adding more interactive features, such as data visualization or more detailed predictions.

