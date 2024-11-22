import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("hello streamlit")

## Disply a simple text
st.write("this is a simple text")

## To create a Simple Data Frame

df = pd.DataFrame({
    'first coloum' : [1,2,3,4,5],
    'second coloum' : [5,10,15,20,25] 
})

# To display a data Frame
st.write("here is the dataframe")
st.write(df)


# To Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ['a','b','c']
)
st.line_chart(chart_data)