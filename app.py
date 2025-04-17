import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    file_path = "portfolio_with_benchmark_and_contributions.xlsx"
    df = pd.read_excel(file_path, index_col=0, parse_dates=True)
    return df

df = load_data()

# Title
st.title("📊 Portfolio Performance Dashboard")

# Portfolio Performance vs Benchmark
st.subheader("Portfolio vs NIFTY 50 Benchmark")
fig1, ax1 = plt.subplots(figsize=(10, 5))
df['Portfolio_Value'].plot(ax=ax1, label='Portfolio (No Contributions)')
df['Portfolio_With_Contributions'].plot(ax=ax1, label='Portfolio (With Contributions)')
df['NIFTY_50'].plot(ax=ax1, label='NIFTY 50 Benchmark')
ax1.set_xlabel("Date")
ax1.set_ylabel("Normalized Value")
ax1.legend()
ax1.grid(True)
st.pyplot(fig1)

# Monthly Contributions
st.subheader("Monthly & Cumulative Contributions")
fig2, ax2 = plt.subplots(figsize=(10, 5))
df['Total_Contributions'].plot(ax=ax2, label='Cumulative Contributions')
ax2.set_xlabel("Date")
ax2.set_ylabel("INR")
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

# Final Portfolio Breakdown
st.subheader("Final Portfolio Breakdown")
final_weights = df[[col for col in df.columns if col.startswith("Weight_")]].iloc[-1]
fig3, ax3 = plt.subplots()
final_weights.plot(kind='bar', ax=ax3)
ax3.set_ylabel("Weighted Value")
ax3.set_title("Final Stock Allocation")
st.pyplot(fig3)

# Raw Data Toggle
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data Table")
    st.write(df.tail(30))
