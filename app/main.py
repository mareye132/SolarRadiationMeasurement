import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sidebar for user input
st.sidebar.header("User Input")

# **Updated Section**: Upload the CSV file
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # **Updated Section**: Read the CSV file from the uploaded file
    df = pd.read_csv(uploaded_file)
    selected_feature = st.sidebar.selectbox("Select feature", df.columns)

    # Main Panel
    st.title("Dashboard")
    st.write("Displaying data and visualizations")

    # Plotting
    fig, ax = plt.subplots()
    sns.histplot(df[selected_feature], ax=ax, bins=30)
    st.pyplot(fig)
else:
    # **Updated Section**: Display message if no file is uploaded
    st.write("Please upload a CSV file to continue.")
