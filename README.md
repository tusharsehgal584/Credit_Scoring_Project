# Credit Scoring Project

A machine learning-powered web app for predicting the credit default risk of loan applicants. Built with Flask and scikit-learn, this project demonstrates the complete workflow of credit scoring—from data analysis and model training to web deployment.

---

## 🚀 Features

- **Credit Default Risk Prediction:** Instantly predicts if an applicant is at high or low risk of defaulting on a loan.
- **Machine Learning Backend:** Uses a scikit-learn model (`credit_model.pkl`) trained on real loan data.
- **User-Friendly Web Interface:** Simple HTML form for data entry and result display.
- **Reusable Structure:** Organized for easy extension and deployment.

---

## 🗂️ Project Structure


![image](https://github.com/user-attachments/assets/203fcf0f-d6b0-452e-9bbb-b458fe78f922)


---

## ⚙️ Getting Started

### Prerequisites

- Python 3.7 or above
- pip (Python package installer)

### Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/tusharsehgal584/Credit_Scoring_Project.git
    cd Credit_Scoring_Project
    ```

2. **(Optional) Create a virtual environment:**
    ```
    python -m venv .venv
    source .venv/bin/activate   # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```
    pip install -r requirement.txt
    ```

4. **Run the application:**
    ```
    python app.py
    ```
    The app will be available at [http://127.0.0.1:8080](http://127.0.0.1:8080).

---

## 💻 Usage

1. Open your browser and go to [http://127.0.0.1:8080](http://127.0.0.1:8080).
2. Enter applicant details (Log of Income, Log of Loan Amount, Term, Credit History).
3. Click **Predict** to see if the applicant is at "High Default Risk" or "Low Default Risk".

---

## 📊 Model & Data

- **Dataset:** `data/loan_data.csv`  
  Contains historical loan applicant data used for model training.
- **Model:** `model/credit_model.pkl`  
  A scikit-learn model (e.g., Logistic Regression, Decision Tree, etc.) trained to classify credit risk.
- **Notebook:**  
  Model training and evaluation steps are documented in `notebook/Credit_Scoring_Model (2).ipynb`.

---

## 📝 File Descriptions

- `app.py` – Main Flask web application for prediction.
- `model/credit_model.pkl` – Pre-trained credit scoring model (pickle format).
- `templates/index.html` – HTML template for user input and result display.
- `data/loan_data.csv` – Dataset used for model training.
- `notebook/Credit_Scoring_Model (2).ipynb` – Jupyter notebook for data exploration and model building.
- `requirement.txt` – List of required Python packages.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

- [Tushar Sehgal](https://github.com/tusharsehgal584)
- Student at Amity University, Greater Noida

---

