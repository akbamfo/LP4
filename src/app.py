import streamlit as st
 
st.write("""
# Customer Churn Prediction
## This app was developed for the sole purpose to predict if given certain inputs, an *existing customer* would likely *churn* or exit

""")
st.text_input('Enter your name')
st.number_input('Enter your age')
st.text_input('Enter specie type ')
st.number_input('Enter which category')
st.text_input('Enter some text')
st.number_input('Enter a number')
st.button('Hit me')