import streamlit as st
from datetime import datetime

def add_log(message: str):
    if 'logs' not in st.session_state:
        st.session_state.logs = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.logs.append(f"{timestamp} - {message}")