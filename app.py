import streamlit as st
st.write("Hello")

st.header("Header")
st.write("Message")

st.number_input("Enter monthly Sales Target in (USD):",
                min_value=0,
                max_value=100000,
                value=50000)
