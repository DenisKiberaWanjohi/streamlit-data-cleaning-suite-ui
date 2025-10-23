import streamlit as st
from modules import combine, split, clean, logs, support
from utils.logger import add_log

st.set_page_config(page_title="Data Cleaning Dashboard", page_icon="🧹", layout="wide")

if 'active_tool' not in st.session_state:
    st.session_state.active_tool = None
if 'logs' not in st.session_state:
    st.session_state.logs = []

st.sidebar.title("Navigation")
nav_choice = st.sidebar.radio("Go to:", ["🏠 Dashboard", "📜 Logs", "❓ Support"], index=0)

if nav_choice != "🏠 Dashboard":
    st.session_state.active_tool = None

if nav_choice == "🏠 Dashboard":
    if st.session_state.active_tool is None:
        st.title("🧰 Data Cleaning Tools")
        st.markdown("Use the tools below to combine, split, or clean your datasets.")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("📎 Combine Files")
            st.write("Merge multiple CSV or Excel files into one dataset.")
            if st.button("Launch Tool", key="combine_btn"):
                st.session_state.active_tool = "combine"
                st.experimental_rerun()
        with col2:
            st.subheader("✂️ Split File")
            st.write("Split a file by row count or unique column values.")
            if st.button("Launch Tool", key="split_btn"):
                st.session_state.active_tool = "split"
                st.experimental_rerun()
        with col3:
            st.subheader("🧹 Clean Special Characters")
            st.write("Remove or replace unwanted characters in your text columns.")
            if st.button("Launch Tool", key="clean_btn"):
                st.session_state.active_tool = "clean"
                st.experimental_rerun()
    else:
        if st.session_state.active_tool == "combine":
            combine.run_combine_tool()
        elif st.session_state.active_tool == "split":
            split.run_split_tool()
        elif st.session_state.active_tool == "clean":
            clean.run_clean_tool()

        if st.button("⬅️ Back to Dashboard"):
            st.session_state.active_tool = None
            st.experimental_rerun()

elif nav_choice == "📜 Logs":
    logs.show_logs_page()

elif nav_choice == "❓ Support":
    support.show_support_page()