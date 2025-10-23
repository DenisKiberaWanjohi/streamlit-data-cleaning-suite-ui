import streamlit as st

def show_logs_page():
    st.header("📜 Application Logs")
    logs = st.session_state.get('logs', [])
    if logs:
        st.text_area("Event Log", value="\n".join(logs), height=300)
    else:
        st.info("No logs yet. Run a tool to generate some activity.")
