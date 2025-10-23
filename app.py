import streamlit as st
from modules import combine, split, clean, logs, support
from utils.logger import add_log

st.set_page_config(page_title="Data Cleaning Dashboard", page_icon="🧹", layout="wide")

# Initialize session state
if 'active_tool' not in st.session_state:
    st.session_state.active_tool = None
if 'logs' not in st.session_state:
    st.session_state.logs = []

# Sidebar navigation
st.sidebar.title("Navigation")
nav_choice = st.sidebar.radio("Go to:", ["🏠 Dashboard", "📜 Logs", "❓ Support"], index=0)

# Reset tool state on non-dashboard pages
if nav_choice != "🏠 Dashboard":
    st.session_state.active_tool = None

# Main content
if nav_choice == "🏠 Dashboard":
    if st.session_state.active_tool is None:
        st.title("🧰 Data Cleaning Tools")
        st.markdown("Use the tools below to combine, split, or clean your datasets.")

        # Style for uniform height cards
        card_style = """
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 1.5rem;
            background-color: #fff;
            box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        """

        col1, col2, col3 = st.columns(3)

        with col1:
            with st.container():
                st.markdown(f"<div style='{card_style}'>", unsafe_allow_html=True)
                st.markdown("### 📎 Combine Files", unsafe_allow_html=True)
                st.markdown("<p style='font-size: 0.9rem;'>Merge multiple CSV or Excel files into one dataset.</p>", unsafe_allow_html=True)
                combine_clicked = st.button("Launch Tool", key="combine_btn")
                st.markdown("</div>", unsafe_allow_html=True)
            if combine_clicked:
                st.session_state.active_tool = "combine"

        with col2:
            with st.container():
                st.markdown(f"<div style='{card_style}'>", unsafe_allow_html=True)
                st.markdown("### ✂️ Split File", unsafe_allow_html=True)
                st.markdown("<p style='font-size: 0.9rem;'>Split a file by row count or unique column values.</p>", unsafe_allow_html=True)
                split_clicked = st.button("Launch Tool", key="split_btn")
                st.markdown("</div>", unsafe_allow_html=True)
            if split_clicked:
                st.session_state.active_tool = "split"

        with col3:
            with st.container():
                st.markdown(f"<div style='{card_style}'>", unsafe_allow_html=True)
                st.markdown("### 🧹 Clean Special Characters", unsafe_allow_html=True)
                st.markdown("<p style='font-size: 0.9rem;'>Remove or replace unwanted characters in your text columns.</p>", unsafe_allow_html=True)
                clean_clicked = st.button("Launch Tool", key="clean_btn")
                st.markdown("</div>", unsafe_allow_html=True)
            if clean_clicked:
                st.session_state.active_tool = "clean"

    else:
        tool = st.session_state.active_tool
        if tool == "combine":
            combine.run_combine_tool()
        elif tool == "split":
            split.run_split_tool()
        elif tool == "clean":
            clean.run_clean_tool()

        st.write("")
        if st.button("⬅️ Back to Dashboard"):
            st.session_state.active_tool = None

elif nav_choice == "📜 Logs":
    logs.show_logs_page()

elif nav_choice == "❓ Support":
    support.show_support_page()
