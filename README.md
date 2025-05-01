# CMPSC445Project2
[https://norepy0317.github.io/CMPSC445Project2/](https://tariff-price.onrender.com/)

While it is impossible to predict tariffs, as they are policy based made by the individuals of the government and do not follow any set rules with how much a product will be taxed, we can predict their impact on the price of a product. This program does just that, as it predicts the price increase of steel based on how prices in the past affected the market. This will predict how tariffs will impact the steel industry and help people plan accordingly. The Steel Tariff Impact Predictor is a practical web application designed to help businesses and analysts estimate how tariffs will affect the steel pricing and market, helping them plan their budget around the tariffs.

The code follows a logical structure for easy maintenance and scalability. At its core, app.py handles web requests and predictions, while the templates/index.html file renders the user interface. The machine learning model, trained on synthetic data simulating various tariff scenarios, is integrated directly into the Flask application. Key dependencies like skylearn for modeling and pandas for data handling are documented in requirements.txt, ensuring smooth deployment.

<img width="900" alt="Screenshot 2025-05-01 at 5 37 33 PM" src="https://github.com/user-attachments/assets/c60992da-7d47-43e7-9fd6-921a92bce61a" />


Using the tool is straightforward and simple. Users enter two values: the base price of the steel (in dollars per ton) and the tariff percentage they want to evaluate. With a click of the "Calculate" button, the system computes and displays both the expected price increase and the new total price with the tariff. The clean, responsive interface works on any device, requiring no technical expertise. For example, entering a base price of 1,000 with a tariff of 23%, the program predicts there will be a $226.61 price increase and calculates the new price before displaying this information to the user. Additionally, to prevent errors, the user has been prevented from entering tariffs bellow 0% or base prices bellow 0%.
￼
<img width="506" alt="Steel Price Calculator" src="https://github.com/user-attachments/assets/6aefacd0-80fb-4bec-8346-616dea410d8b" />


The dataset, though synthetic, was carefully designed to reflect realistic market conditions. It includes ten examples covering different base prices and tariff rates. Each entry specifies the corresponding price increase, allowing the model to learn the direct relationship between tariffs and steel costs. While limited in size, this data suffices for demonstrating the proof of concept, with room to incorporate larger, real-world datasets in future iterations. The reason for the use of synthetic data is that sites that contain data on the tariffs and prices of the products before and after the tariffs have ant-scraping features that prevent us from gathering the data directly from their site. Due to this method of data, data preprocessing is not needed, however if this project were to be expanded upon and larger quantities of data gathered, outliers would need to be filtered out of the data being used. 

A linear regression model was chosen for its interpretability and computational efficiency. It takes base price and tariff percentage as inputs, outputting the predicted dollar increase. Testing showed strong performance, though this reflects the intentionally linear relationship in the training set. In practice, more complex models might be needed to capture nonlinear tariff effects or additional variables like transportation costs.

This project highlights several valuable lessons. First, even simple machine learning models can deliver immediate business value when paired with accessible interfaces. Second, synthetic data—while useful for prototyping—has limitations compared to real-world observations. We faced challenges like ensuring proper Flask template rendering and handling user inputs and the difficulties of finding accessible large and reliable data to pull from.

Ultimately, the Steel Tariff Impact Predictor succeeds as a clear, functional demonstration of applied machine learning. Its modular design allows for easy expansion, such as adding regional pricing data or currency conversion. Future work could integrate live steel market feeds or advanced modeling techniques, but the current version already achieves its goal: making tariff consequences tangible for decision-makers.

