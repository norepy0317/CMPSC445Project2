# CMPSC445Project2
[https://norepy0317.github.io/CMPSC445Project2/](https://tariff-price.onrender.com/)

The objective of this project is to create code that can predict the price increase of products have have tarriffs placed on them based on how the prices of products that had tariffs placed on them in the past. This will help predict the impact of tariffs in the future or current day and help people plan accordingly.

The Steel Tariff Impact Predictor is a practical web application designed to help businesses and analysts estimate how import tariffs affect steel pricing. Built using Python's Flask framework and machine learning, this tool addresses a real-world economic challenge by providing instant price calculations when tariffs are applied. The project combines data science with web development, demonstrating how machine learning can be deployed in user-friendly interfaces to solve tangible problems.

Understanding tariff impacts is crucial for industries reliant on steel imports, from construction to automotive manufacturing. While many pricing tools exist, few focus specifically on tariff effects using predictive modeling. This application fills that gap by offering a simple yet accurate way to forecast price changes, helping businesses make informed purchasing decisions. The use of linear regression—a fundamental machine learning technique—ensures transparency in predictions while maintaining computational efficiency.

Using the tool is straightforward. Visitors enter two values: the base price of steel (in dollars per ton) and the tariff percentage they want to evaluate. With a click of the "Calculate" button, the system computes and displays both the expected price increase and the new total price. The clean, responsive interface works on any device, requiring no technical expertise. For example, entering a base price of 1,000 with a 250 increase, resulting in a new price of $1,250 per ton.

The code follows a logical structure for easy maintenance and scalability. At its core, app.py handles web requests and predictions, while the templates/index.html file renders the user interface. The machine learning model, trained on synthetic data simulating various tariff scenarios, is integrated directly into the Flask application. Key dependencies like scikit-learn for modeling and pandas for data handling are documented in requirements.txt, ensuring smooth deployment.

Functionality was rigorously tested during development. The model accurately predicts price changes based on the training data, with manual verification confirming correct calculations for edge cases (e.g., zero tariffs or unusually high base prices). The web interface underwent cross-browser testing to guarantee consistent performance. Notably, the system prevents invalid inputs—like negative prices—through front-end validation and error handling.

The dataset, though synthetic, was carefully designed to reflect realistic market conditions. It includes ten examples covering different base prices (
800
–
800–1,500/ton) and tariff rates (0–25%). Each entry specifies the corresponding price increase, allowing the model to learn the direct relationship between tariffs and steel costs. While limited in size, this data suffices for demonstrating the proof of concept, with room to incorporate larger, real-world datasets in future iterations.

Data processing was minimal but intentional. The raw numbers required no cleaning, but critical feature engineering ensured the model could generalize beyond the training examples. By using both the base price and tariff percentage as inputs—rather than just one variable—the system accounts for how the same tariff rate affects different initial prices. This approach mirrors real economic behavior where absolute price increases scale with base costs.

A linear regression model was chosen for its interpretability and computational efficiency. It takes base price and tariff percentage as inputs, outputting the predicted dollar increase. Testing showed strong performance (R² = 1.0 on the synthetic data), though this perfect score reflects the intentionally linear relationship in the training set. In practice, more complex models might be needed to capture nonlinear tariff effects or additional variables like transportation costs.

This project highlights several valuable lessons. First, even simple machine learning models can deliver immediate business value when paired with accessible interfaces. Second, synthetic data—while useful for prototyping—has limitations compared to real-world observations. Challenges like ensuring proper Flask template rendering and handling user inputs reinforced the importance of defensive programming. The application directly applies course concepts like regression modeling and model deployment, bridging the gap between theory and implementation.

Ultimately, the Steel Tariff Impact Predictor succeeds as a clear, functional demonstration of applied machine learning. Its modular design allows for easy expansion, such as adding regional pricing data or currency conversion. Future work could integrate live steel market feeds or advanced modeling techniques, but the current version already achieves its goal: making tariff consequences tangible for decision-makers. By combining clean code, thoughtful design, and explainable AI, this project exemplifies how technical skills can solve concrete problems.

