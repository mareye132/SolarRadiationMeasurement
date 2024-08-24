import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache
def load_data():
    # Replace with your data loading logic
    return pd.read_csv('C:\Users\user\Desktop\Github\Dahboard_Development\app\iris.csv')

df = load_data()

# Sidebar for user input
st.sidebar.header("User Input")
selected_feature = st.sidebar.selectbox("Select feature", df.columns)

# Main Panel
st.title("Dashboard")
st.write("Displaying data and visualizations")

# Plotting
fig, ax = plt.subplots()
sns.histplot(df[selected_feature], ax=ax, bins=30)
st.pyplot(fig)

# Add more interactive elements and visualizations as needed
