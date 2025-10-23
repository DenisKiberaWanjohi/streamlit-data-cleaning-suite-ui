import streamlit as st

# Page config for wide layout
st.set_page_config(page_title="Tool Dashboard", layout="wide")

# Inject CSS for card styling and layout fixes
st.markdown("""
<style>
/* Style each column as a card */
[data-testid="column"] {
  background-color: #F9F9F9;  /* light grey card background */
  border: 1px solid #DDDDDD;  /* subtle border for card outline */
  border-radius: 8px;
  padding: 20px;
  display: flex;
  flex-direction: column;
}
/* Remove extra top margin on headings inside cards for tight spacing */
[data-testid="column"] h1, [data-testid="column"] h2,
[data-testid="column"] h3, [data-testid="column"] h4 {
  margin-top: 0.1em;
}
/* Ensure paragraph text in cards has consistent spacing */
[data-testid="column"] p {
  margin-bottom: 1em;
}
/* Push the button container to bottom of the card */
[data-testid="column"] div.stButton {
  margin-top: auto;
  text-align: right;  /* align button to right within card (optional) */
}
/* Style the actual button element */
[data-testid="column"] button {
  background-color: #2E6EF7;  /* primary color for Launch button */
  color: white;
  padding: 0.5em 1em;
  border: none;
  border-radius: 5px;
  font-weight: 600;
  cursor: pointer;
}
[data-testid="column"] button:hover {
  background-color: #1E50B5;  /* darker shade on hover */
}
</style>
""", unsafe_allow_html=True)

# Create three equal-width columns for the tool cards
col1, col2, col3 = st.columns(3)  # all columns have equal width:contentReference[oaicite:4]{index=4}

# Tool Card 1: Combine Files
with col1:
    st.subheader("🔗 Combine Files")
    st.write("Merge multiple files (Excel, CSV, etc.) into a single consolidated file. "
             "This tool combines sheets or data tables while preserving formatting.")
    launched1 = st.button("Launch", key="combine_files")
    if launched1:
        st.success("Combine Files tool launched!")

# Tool Card 2: Split File
with col2:
    st.subheader("✂️ Split File")
    st.write("Split a large file into smaller parts. Define custom split criteria, like number of rows or file size, to break down big files for easier handling.")
    launched2 = st.button("Launch", key="split_file")
    if launched2:
        st.success("Split File tool launched!")

# Tool Card 3: Clean Special Characters
with col3:
    st.subheader("🧹 Clean Special Characters")
    st.write("Remove or replace unwanted special characters from your data. Ideal for cleaning text in CSV or Excel files before analysis or import.")
    launched3 = st.button("Launch", key="clean_chars")
    if launched3:
        st.success("Clean Special Characters tool launched!")