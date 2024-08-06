import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('statistics_data.csv')

# Streamlit app
st.title("Interactive Statistics Dashboard")

# User selects the type of diagram
diagram_type = st.selectbox(
    "Choose the type of diagram",
    ("Bar Chart", "Line Chart", "Scatter Plot")
)

# Generate the diagram based on user selection
if diagram_type == "Bar Chart":
    st.header("Bar Chart")
    fig, ax = plt.subplots()
    sns.barplot(x='Category', y='Value1', data=data, ax=ax)
    st.pyplot(fig)

elif diagram_type == "Line Chart":
    st.header("Line Chart")
    fig, ax = plt.subplots()
    sns.lineplot(x='Date', y='Value1', data=data, ax=ax)
    st.pyplot(fig)

elif diagram_type == "Scatter Plot":
    st.header("Scatter Plot")
    fig, ax = plt.subplots()
    sns.scatterplot(x='Value1', y='Value2', hue='Category', data=data, ax=ax)
    st.pyplot(fig)

# Display the data table
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)
