import streamlit as st
import random
import time
import requests

st.title("💰 Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.sidebar.title("💵 Instant Cash Generator")

if st.button("💵 Generate Money"):
    st.write("💸 Counting your Money...")
    time.sleep(5)
    amount = generate_money()
    st.success(f"💰 You have generated ${amount}")


