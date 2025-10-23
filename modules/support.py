import streamlit as st
from utils.logger import add_log

def show_support_page():
    st.header("❓ Support")
    with st.form("support_form"):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Describe your issue")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if name and email and message:
                add_log(f"Support request from {name} ({email}): {message}")
                st.success("Thank you! Your request has been received.")
            else:
                st.warning("Please fill out all fields before submitting.")