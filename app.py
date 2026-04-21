import streamlit as st
import pandas as pd
import joblib

# ---------------- LOAD MODEL ----------------
model = joblib.load("notebooks/model.pkl")
columns = joblib.load("notebooks/columns.pkl")

# ---------------- UI ----------------
st.title("🏠 House Price Prediction App")
st.write("Enter house details to predict price:")

# ---------------- CREATE EMPTY INPUT ----------------
input_data = pd.DataFrame(columns=columns)
input_data.loc[0] = 0  # fill all columns with 0

# ---------------- USER INPUTS ----------------
area = st.number_input("Area", value=1000)
bedrooms = st.number_input("Bedrooms", value=2)
bathrooms = st.number_input("Bathrooms", value=1)
stories = st.number_input("Stories", value=1)
parking = st.number_input("Parking", value=0)

mainroad = st.selectbox("Main Road", ["no", "yes"])
guestroom = st.selectbox("Guest Room", ["no", "yes"])
basement = st.selectbox("Basement", ["no", "yes"])
hotwaterheating = st.selectbox("Hot Water Heating", ["no", "yes"])
airconditioning = st.selectbox("Air Conditioning", ["no", "yes"])
prefarea = st.selectbox("Preferred Area", ["no", "yes"])

furnishing = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)

# ---------------- MAP INPUTS ----------------
input_data["area"] = area
input_data["bedrooms"] = bedrooms
input_data["bathrooms"] = bathrooms
input_data["stories"] = stories
input_data["parking"] = parking

if mainroad == "yes":
    input_data["mainroad_yes"] = 1

if guestroom == "yes":
    input_data["guestroom_yes"] = 1

if basement == "yes":
    input_data["basement_yes"] = 1

if hotwaterheating == "yes":
    input_data["hotwaterheating_yes"] = 1

if airconditioning == "yes":
    input_data["airconditioning_yes"] = 1

if prefarea == "yes":
    input_data["prefarea_yes"] = 1

if furnishing == "semi-furnished":
    input_data["furnishingstatus_semi-furnished"] = 1
elif furnishing == "unfurnished":
    input_data["furnishingstatus_unfurnished"] = 1

# ---------------- PREDICT ----------------
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted Price: {prediction[0]:,.2f}")