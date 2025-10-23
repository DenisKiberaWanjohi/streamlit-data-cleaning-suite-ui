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

# Reset tool when leaving dashboard
if nav_choice != "🏠 Dashboard":
    st.session_state.active_tool = None

# Main content
if nav_choice == "🏠 Dashboard":
    if st.session_state.active_tool is None:
        st.title("🧰 Data Cleaning Tools")
        st.markdown("Use the tools below to combine, split, or clean your datasets.")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
                <div style='border: 1px solid #ccc; border-radius: 10px; padding: 1.5rem 1rem 1rem 1rem;
                            background-color: #fff; box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
                            text-align: center; min-height: 220px; display: flex; flex-direction: column; justify-content: space-between;'>
                    <div>
                        <h3 style='margin-bottom: 0.5rem;'>📎 Combine Files</h3>
                        <p style='font-size: 0.9rem;'>Merge multiple CSV or Excel files into one dataset.</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
            if st.button("Launch Tool", key="combine_btn"):
                st.session_state.active_tool = "combine"

        with col2:
            st.markdown("""
                <div style='border: 1px solid #ccc; border-radius: 10px; padding: 1.5rem 1rem 1rem 1rem;
                            background-color: #fff; box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
                            text-align: center; min-height: 220px; display: flex; flex-direction: column; justify-content: space-between;'>
                    <div>
                        <h3 style='margin-bottom: 0.5rem;'>✂️ Split File</h3>
                        <p style='font-size: 0.9rem;'>Split a file by row count or unique column values.</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
            if st.button("Launch Tool", key="split_btn"):
                st.session_state.active_tool = "split"

        with col3:
            st.markdown("""
                <div style='border: 1px solid #ccc; border-radius: 10px; padding: 1.5rem 1rem 1rem 1rem;
                            background-color: #fff; box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
                            text-align: center; min-height: 220px; display: flex; flex-direction: column; justify-content: space-between;'>
                    <div>
                        <h3 style='margin-bottom: 0.5rem;'>🧹 Clean Special Characters</h3>
                        <p style='font-size: 0.9rem;'>Remove or replace unwanted characters in your text columns.</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
            if st.button("Launch Tool", key="clean_btn"):
                st.session_state.active_tool = "clean"

    else:
        # Run the selected tool
        if st.session_state.active_tool == "combine":
            combine.run_combine_tool()
        elif st.session_state.active_tool == "split":
            split.run_split_tool()
        elif st.session_state.active_tool == "clean":
            clean.run_clean_tool()

        if st.button("⬅️ Back to Dashboard"):
            st.session_state.active_tool = None

elif nav_choice == "📜 Logs":
    logs.show_logs_page()

elif nav_choice == "❓ Support":
    support.show_support_page()