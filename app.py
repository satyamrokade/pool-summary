import streamlit as st
import pandas as pd

# Streamlit app
st.title("Upload Offered Pool Data (DA Business)")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    # Cleaning: Make sure numeric columns are correct (in case ₹ symbol or commas)
    df['POS'] = df['POS'].replace('[₹,]', '', regex=True).astype(float)
    # df['Average_Ticket_Size'] = df['Average_Ticket_Size'].replace('[₹,]', '', regex=True).astype(float)

    # Creating the summary table
    summary = {
        "Total Loan Count": df['LANID'].count(),
        "Min POS (₹)": df['POS'].min(),
        "Max POS (₹)": df['POS'].max(),
        # "Average POS (₹)": df['POS'].sum()/df['LANID'].count(),
        "Min tenure (₹)": df['tenure'].min(),
        "Max tenure (₹)": df['tenure'].max(),
        # "Average tenure (₹)": df['tenure'].mean(),
        # "Average Ticket Size (₹)": df['Average_Ticket_Size'].mean(),
    }

    summary_df = pd.DataFrame.from_dict(summary, orient='index', columns=['Value'])

    st.subheader("Summary Table")
    st.table(summary_df)

else:
    st.write("Please upload a CSV file.")
