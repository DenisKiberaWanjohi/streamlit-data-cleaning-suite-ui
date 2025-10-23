import streamlit as st
from modules import combine, split, clean, logs, support
from utils.logger import add_log

st.set_page_config(page_title="Data Cleaning Dashboard", page_icon="🧹", layout="wide")

# Initialize session state
if 'active_tool' not in st.session_state:
    st.session_state.active_tool = None
if 'logs' not in st.session_state:
    st.session_state.logs = []

# Sidebar
st.sidebar.title("Navigation")
nav_choice = st.sidebar.radio("Go to:", ["🏠 Dashboard", "📜 Logs", "❓ Support"], index=0)

if nav_choice != "🏠 Dashboard":
    st.session_state.active_tool = None

# Main content area
if nav_choice == "🏠 Dashboard":
    if st.session_state.active_tool is None:
        st.title("🧰 Data Cleaning Tools")
        st.markdown("Use the tools below to combine, split, or clean your datasets.")

        # Styling for tool cards
        st.markdown("""
        <style>
        .card {
            border: 1px solid #d3d3d3;
            border-radius: 10px;
            padding: 1rem;
            background-color: #fff;
            box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
            transition: box-shadow 0.2s ease;
        }
        .card:hover {
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        }
        .card h3 {
            margin-top: 0.5rem;
        }
        </style>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            with st.container():
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.markdown("### 📎 Combine Files")
                st.write("Merge multiple CSV or Excel files into one dataset.")
                if st.button("Launch Tool", key="combine_btn"):
                    st.session_state.active_tool = "combine"
                st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            with st.container():
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.markdown("### ✂️ Split File")
                st.write("Split a file by row count or unique column values.")
                if st.button("Launch Tool", key="split_btn"):
                    st.session_state.active_tool = "split"
                st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            with st.container():
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.markdown("### 🧹 Clean Special Characters")
                st.write("Remove or replace unwanted characters in your text columns.")
                if st.button("Launch Tool", key="clean_btn"):
                    st.session_state.active_tool = "clean"
                st.markdown("</div>", unsafe_allow_html=True)

    else:
        # Active tool view
        if st.session_state.active_tool == "combine":
            combine.run_combine_tool()
        elif st.session_state.active_tool == "split":
            split.run_split_tool()
        elif st.session_state.active_tool == "clean":
            clean.run_clean_tool()

        st.write("")
        if st.button("⬅️ Back to Dashboard"):
            st.session_state.active_tool = None

elif nav_choice == "📜 Logs":
    logs.show_logs_page()

elif nav_choice == "❓ Support":
    support.show_support_page()