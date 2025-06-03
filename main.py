import streamlit as st
import numpy as np

st.set_page_config(page_title="Chicken Road Crash Predictor", page_icon="🐔", layout="centered")
st.title("🐔 Chicken Road Crash Predictor")
st.write("Simulate crash rounds and test different cash-out strategies!")

cash_out = st.selectbox("Select Cash-Out Multiplier:", [1.5, 2.0, 3.0, 5.0])
rounds = st.slider("Number of Rounds to Simulate", min_value=100, max_value=10000, step=100, value=1000)

if st.button("Run Simulation"):
    crash_points = np.random.exponential(scale=2.0, size=rounds) + 1.0
    wins = crash_points >= cash_out
    profit = (wins * (cash_out - 1)) - (~wins * 1)
    avg_profit = round(np.mean(profit), 2)
    win_rate = round(100 * np.sum(wins) / rounds, 2)

    st.success(f"Results for cash-out at {cash_out}x:")
    st.write(f"**Average Profit per Round:** {avg_profit}")
    st.write(f"**Win Rate:** {win_rate}%")

    st.line_chart(profit[:200])
