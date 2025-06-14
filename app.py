import streamlit as st
import pandas as pd
import pickle

# load the model and scaler
with open(r"./notebooks/model.pkl", "rb") as f:
    model = pickle.load(f)
with open(r"./notebooks/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("Predicción de precio de alquiler en Madrid")

# user inputs
rooms = st.number_input("Number of rooms", min_value=1, max_value=10, value=2)
area = st.number_input("Square meters", min_value=10, max_value=500, value=50)
floor = st.number_input("Floor", min_value=0, max_value=25, value=0)
pool = st.checkbox("Pool")
furniture = st.checkbox("Furniture")
exterior = st.checkbox("Exterior")
elevator = st.checkbox("Elevator")
district = st.selectbox("District", ["Chueca", "La Latina", "Lavapiés", "Malasaña", "Moncloa"])
property_type = st.selectbox("Type", ["Duplex", "Flat", "Studio"]) 

# Transformación manual
input_df = pd.DataFrame([{
    "Rooms": rooms,
    "Squared_meters": area,
    "Floor": floor,
    "Pool": pool,
    "Furniture": furniture,
    "Exterior": exterior,
    "Elevator": elevator,
    **{f"Distric_{d}": 1 if d == district else 0 for d in ["Chueca", "La Latina", "Lavapies", "Malasaña", "Moncloa"]},
    **{f"Type_{t}": 1 if t == property_type else 0 for t in ["Duplex", "Flat", "Studio"]}
}])


import warnings
warnings.filterwarnings("ignore")


input_scaled = scaler.transform(input_df)
pred = model.predict(input_scaled)[0]

st.success(f"El precio estimado de alquiler es: {round(pred, 2)} €")
