import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ML Prediction App",
    page_icon="📊",
    layout="centered"
)

st.title("📊 ML Prediction Application")
st.write("Upload dataset and enter feature values to get prediction")

# CSV Upload
uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("CSV file uploaded successfully!")
    st.dataframe(df.head())

st.subheader("Enter Feature Values")

# Feature inputs (generic)
f1 = st.number_input("Feature 1", value=0.0)
f2 = st.number_input("Feature 2", value=0.0)
f3 = st.number_input("Feature 3", value=0.0)

if st.button("Predict"):
    # Dummy prediction logic
    prediction = (f1 + f2 + f3) / 3

    st.subheader("Prediction Result")
    st.success(f"Predicted Output: {prediction:.2f}")
