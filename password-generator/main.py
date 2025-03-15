import streamlit as st
import random
import string

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += (
            string.punctuation
        )

    return "".join(random.choice(characters) for _ in range(length))


# Streamlit code
st.title("🔐 Password Generator")

# User input
length = st.slider("Select Password Length:", min_value=6, max_value=30, value=12)

use_digits = st.checkbox("🔢 Include numbers")
use_special = st.checkbox("🔣 Include special characters")

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(
        length,
        use_digits,
        use_special
    )
    st.write(f"🔑 Your Password is: `{password}`")