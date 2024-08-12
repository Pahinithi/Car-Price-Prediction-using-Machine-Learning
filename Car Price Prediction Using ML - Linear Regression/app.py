from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='.')

# Load the trained model
with open("car_price_prediction_model.pkl", "rb") as file:
    model = pickle.load(file)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    # Get input data from form
    year = float(request.form["year"])
    present_price = float(request.form["present_price"])
    kms_driven = float(request.form["kms_driven"])
    fuel_type = int(request.form["fuel_type"])
    seller_type = int(request.form["seller_type"])
    transmission = int(request.form["transmission"])
    owner = int(request.form["owner"])

    # Combine inputs into a numpy array
    input_data = np.asarray([[year, present_price, kms_driven, fuel_type, seller_type, transmission, owner]])

    # Make prediction
    prediction = model.predict(input_data)

    # Format prediction result
    prediction_text = f'Predicted Selling Price: {prediction[0]:.2f} lakhs'

    return render_template("index.html", prediction=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
