import streamlit as st

st.title("Retail Business Dashboard")

st.header("Manager Input Section")
st.write("Please enter the montly sales target and select the regoin")

sales = st.number_input("Enter Monthly Sales Target(in USD):",
                                                      min_value=0,
                                                      max_value=100000,
                                                      Value = 50000)


