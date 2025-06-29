# Madrid_rental_price_prediction

---

## Description
This project uses a dataset obtained from Kaggle, generated through a scraper of Idealista, to predict the rental price of housing in Madrid. The prediction is made based on the data entered by the user through a web application developed with Streamlit.

---

## Requirements / Dependencies
- Python (recommended version: 3.8+)
- pandas
- scikit-learn
- streamlit
- pickle

All required libraries are listed in the `requirements.txt` file.

---

## Installation
1. Clone this repository:  
   `git clone https://github.com/tene04/Madrid_rental_price_prediction.git`  
   `cd Madrid_rental_price_prediction`

2. Install the dependencies:  
   `pip install -r requirements.txt`

---

## Execution
To launch the web application, open a terminal, navigate to the folder (where `app.py` is located), and run:  
`streamlit run app.py`  
Then, open your browser at the URL provided by Streamlit (usually http://localhost:8501).

---

## Project Structure
Madrid_rental_price_prediction/  
```text
├── data/                   # Original data in CSV format  
│   └── dataset.csv  
├── notebooks/              # Notebook with EDA, preprocessing, and model training  
│   └── exploracion.ipynb  
│   └── model.pkl           # Trained serialized model  
│   └── scaler.pkl          # Applied normalization  
├── app.py                  # Streamlit application that loads the model and makes predictions  
├── requirements.txt        # Project dependencies  
└── README.md               # This file
```

---

## Basic Usage
Run the app as described in the **Execution** section. In the Streamlit web interface, input the required data. The app will automatically display the estimated rental price in Madrid based on the provided information.
