import streamlit as st
import pandas as pd


name = st.text_input("enter your name: ")

if name:
    st.write(f"Hello {name}")

age = st.slider("select your age: ",0, 100, 23)

st.write(f"Your age is : {age}")

opt = ["python", "java", "c++"]
choice = st.selectbox("choose your fav language: ", opt)
st.write(f"your choice is: {choice}")


# create a csv file
data = {
    "name": ["john", "mohit", "jack"],
    "age" : [23,25,26],
    "city": ["jab", "mum", "pun"]

}

df = pd.DataFrame(data)
df.to_csv("sample.csv")



# To upload a file

uploaded_file = st.file_uploader("choose a CSV file", type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
