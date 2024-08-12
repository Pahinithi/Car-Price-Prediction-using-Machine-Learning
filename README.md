# Car Price Prediction using Machine Learning

This project is a web application that predicts the selling price of a car based on various features using a Linear Regression model. The application is built with Flask and provides a simple interface for users to input the details of the car and get the predicted price.

## Features

- **Linear Regression Model**: The model is trained using a dataset containing car prices and their respective features. It is capable of predicting the price based on user input.
- **Web Interface**: A user-friendly web interface is provided for inputting the car details and viewing the predicted price.
- **Inputs**: The model takes the following inputs:
  - Year of Purchase
  - Present Price (in lakhs)
  - Kilometers Driven
  - Fuel Type (Petrol/Diesel/CNG)
  - Seller Type (Dealer/Individual)
  - Transmission Type (Manual/Automatic)
  - Number of Previous Owners

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pahinithi/Car-Price-Prediction-using-Machine-Learning
   ```
2. **Navigate to the project directory:**
   ```bash
   cd car-price-prediction
   ```
3. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```
4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
5. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run the Flask application:**
   ```bash
   python app.py
   ```
7. **Access the web application:**
   Open a web browser and navigate to `http://127.0.0.1:5000/` to use the car price prediction tool.

## Model Details

- **Algorithm**: Linear Regression
- **Input Features**: The model uses the following features for prediction:
  - Year of Purchase
  - Present Price (in lakhs)
  - Kilometers Driven
  - Fuel Type (Petrol, Diesel, CNG)
  - Seller Type (Dealer, Individual)
  - Transmission Type (Manual, Automatic)
  - Number of Previous Owners

## File Structure

- `app.py`: The main Flask application file.
- `index.html`: The HTML file for the web interface.
- `car_price_prediction_model.pkl`: The pre-trained Linear Regression model saved as a pickle file.
- `requirements.txt`: A list of dependencies required to run the project.

## Usage

1. Input the details of the car into the web form.
2. Submit the form to get the predicted selling price of the car.

## Acknowledgments

This project was developed by **Nithilan**.

## License

This project is licensed under the MIT License.
