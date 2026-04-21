# Credit Scoring System

A web‑based credit scoring system that predicts the creditworthiness of loan applicants using a trained machine‑learning model and serves predictions via a Flask web interface. This project demonstrates an end‑to‑end pipeline from data preprocessing to model deployment.

## 🔧 Features

- Predicts whether a loan applicant is likely to default (credit risk).
- Uses a pre‑trained machine‑learning model (e.g., Random Forest, XGBoost, or Logistic Regression) saved as `model/credit_model.pkl`.
- Web interface built with **Flask** and HTML/CSS templates (`/templates/index.html`).
- Interactive form for user input (age, income, employment status, loan amount, etc.).
- CSV dataset `data/loan_data.csv` used for training and evaluation.
- Simple, clean UI for viewing the prediction result.

## 📦 Project Structure
Credit_Scoring_Project/
├── app.py # Flask backend
├── data/
│ └── loan_data.csv # Loan‑applicant dataset
├── model/
│ └── credit_model.pkl # Trained ML model
├── notebook/
│ └── Credit_Scoring_Model (2).ipynb # Jupyter notebook for training
├── requirements.txt # Python dependencies
└── templates/
└── index.html # Web interface


## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/tusharsehgal584/Credit_Scoring_Project.git
   cd Credit_Scoring_Project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and go to:
5. http://127.0.0.1:5000

6. 
5. Fill in the form with applicant details and submit to get a **credit risk prediction** (e.g., “High Risk” / “Low Risk”).

## 📚 Technologies Used

- **Python** – Core language
- **Flask** – Backend web framework
- **Scikit‑learn / XGBoost** – Model training (shown in `Credit_Scoring_Model (2).ipynb`)
- **Jupyter Notebook** – Exploratory data analysis and model prototyping
- **HTML/CSS** – Frontend interface
- **Pandas, NumPy** – Data preprocessing and handling

## 🎓 Purpose & Learning

This project was created to:
- Understand end‑to‑end credit‑risk modeling for loan applicants.
- Learn how to train, save, and load an ML model.
- Practice deploying an ML model via a simple web interface.
- Gain hands‑on experience in data preprocessing, feature engineering, and model evaluation.

## 🖼️ Demo (example)

A simple screenshot of the web form can be added here later (optional).  
The form typically includes:
- Personal details (age, employment status, etc.)
- Financial details (income, loan amount, existing debts)
- A submit button that returns a risk prediction.

## 📄 License

This project is for educational and personal use. You are free to learn from and modify the code, but please give proper credit to the author.

---

*Built by Tushar Sehgal using Python, Flask, and machine‑learning.*
