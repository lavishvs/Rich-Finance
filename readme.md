# 📊 Rich Finance: Credit Risk Modelling App

A Streamlit web application for predicting credit risk using machine learning. Enter customer and loan details to estimate the probability of default.

---
# Working 
https://rich-finance.streamlit.app/

## 🚀 Features

- User-friendly web interface (Streamlit)
- Predicts credit risk based on user input
- Uses a trained ML model (`model_data.joblib`)
- Visualizes risk and key metrics

---

## 🗂️ Project Structure

```
app/
│
├── main.py                  # Streamlit app main file
├── prediction_helper.py     # Helper functions for prediction
├── Credit_Risk_Model.ipynb  # Model training and analysis notebook
│
├── artifacts/
│   └── model_data.joblib    # Trained ML model
│
├── Data/
│   ├── bureau_data.csv
│   ├── customers.csv
│   └── loans.csv
│
└── __pycache__/
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/<your-username>/<repo-name>.git
    cd <repo-name>/app
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(Create `requirements.txt` if not present: see below)*

3. **Run the app**
    ```bash
    streamlit run main.py
    ```

---

## 📝 Example `requirements.txt`

```
streamlit
scikit-learn
joblib
pandas
numpy
matplotlib
```

---

## 📂 Data & Model

- Place your trained model in `artifacts/model_data.joblib`
- Place input data in the `Data/` folder if needed

---

## ✨ Usage

1. Open the app in your browser (Streamlit will provide a local URL).
2. Enter customer and loan details.
3. Click **"Calculate Risk"** to see the predicted probability of default.

---

## 🧑‍💻 Authors

Made with ❤️ by Rich Finance

---

## 📄 License

This project is for educational purposes.
