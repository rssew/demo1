import streamlit as st

st.title("Retail Business Dashboard")

st.header("Manager Input Section")
st.write("Please enter the montly sales target and select the region")

sales = st.number_input("Enter Monthly Sales Target(in USD):",
                        min_value=0,
                        max_value=100000,
                        value=50000)


