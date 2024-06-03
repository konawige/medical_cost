import streamlit as st
import pandas as pd
from prediction import predict
import time

def click_button():
    st.session_state.clicked = True

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def calc_charges():
    data = {
    'age': [age],
    'bmi': [bmi],
    'children': [children],
    'region': [region],
    'sex': [gender],
    'smoker': [smoker],
      
    }

    df = pd.DataFrame(data)
    prediction = predict(df)
    
    return prediction[0]



st.title("Predicting insurance charges")
st.markdown("Random forest regression model to predict insurance charges")

col1, col2 = st.columns(2)
with col1:
    st.text("Physical attributes")
    gender = st.selectbox("Gender", ["male","female"])
    age = st.number_input("Age", min_value=18, max_value=64, value=25)
    bmi = st.number_input("BMI", min_value=16, max_value=53, value=20)  
with col2:
    st.text("Other attributes")
    children = st.number_input("Children", min_value=0, max_value=5, value=1)
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

st.button("Submit", key="predict", on_click=click_button)


result_text = st.empty()

if st.session_state.clicked:
    result_text.empty()
    with st.spinner("Predicting insurance charges..."):
        time.sleep(3)

    result_text.success(f"The predicted insurance charge is ${calc_charges():.2f}")
    
    st.session_state.clicked = False

