import streamlit as st
import pandas as pd

st.write("""
# Customer Churn Prediction
""")
st.image('src\\image1.jpg')
st.write("""
## This app was developed for the sole purpose to predict if given certain inputs, an *existing customer* would likely *churn* or exit
""")

# Input data
a = st.text_input('Enter your name')
b = st.number_input('Enter your age')
c = st.text_input('Enter specie type ')
d = st.number_input('Enter which category')
e = st.text_input('Enter some text')
f = st.number_input('Enter a number')

# Prediction Button
if st.button('Hit me'):
    df = pd.DataFrame(
            {
            " ":[a], " ":[b], " ":[c], " ":[d], " ":[e], " ":[f],
            }
    )
    print(f"[info] Input data as dataframe:\n {df.to_text()}")
    st.text(f"Thank you, your prediction is: '{''}'")