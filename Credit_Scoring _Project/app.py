from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load trained model
with open("model/credit_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            float(request.form['log_income']),
            float(request.form['log_loan_amount']),
            float(request.form['term_binary']),
            float(request.form['credit_history'])
        ]
        prediction = model.predict([features])[0]
        result = "High Default Risk" if prediction == 1 else "Low Default Risk"
        return render_template("index.html", prediction_text=f"Prediction: {result}")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Change port here (e.g., 8080). Use '0.0.0.0' to allow external access if needed.
    app.run(host='127.0.0.1', port=8080, debug=True)
