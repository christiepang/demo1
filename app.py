import streamlit as st
import pandas as st
import os

current_directory=os.getcwd()
file_path = os.path.join(current_directory,"winequality-red.csv")

df = pd.read_csv(file_path, delimiter=';')

st.write("Wine Quality Data") 
st.dataframe(df) #two D data, function and properties
