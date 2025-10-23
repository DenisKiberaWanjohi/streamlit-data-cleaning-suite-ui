import streamlit as st
import pandas as pd
import zipfile
import io
from utils.logger import add_log

def run_split_tool():
    st.header("✂️ Split File")
    uploaded_file = st.file_uploader("Upload a CSV or Excel file:", type=["csv", "xlsx"])
    split_mode = st.radio("Split method", ["By row count", "By column value"])

    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            sheet = st.text_input("Sheet name (for Excel)", value="Sheet1")
            try:
                df = pd.read_excel(uploaded_file, sheet_name=sheet)
            except Exception as e:
                st.error(f"Failed to load Excel sheet: {e}")
                return

        if split_mode == "By row count":
            chunk_size = st.number_input("Rows per file", min_value=1, value=5000, step=100)
            if st.button("Split by Row Count"):
                chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as zipf:
                    for i, chunk in enumerate(chunks):
                        csv_data = chunk.to_csv(index=False).encode('utf-8')
                        zipf.writestr(f"chunk_{i+1}.csv", csv_data)
                zip_buffer.seek(0)
                add_log(f"Split {uploaded_file.name} into {len(chunks)} chunks by row count.")
                st.success(f"Split into {len(chunks)} files.")
                st.download_button("Download ZIP", data=zip_buffer, file_name="split_files.zip", mime="application/zip")

        elif split_mode == "By column value":
            col = st.selectbox("Select column to split by", df.columns)
            if st.button("Split by Column"):
                groups = dict(tuple(df.groupby(col)))
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as zipf:
                    for val, group_df in groups.items():
                        safe_val = str(val).replace("/", "-").replace(" ", "_")
                        csv_data = group_df.to_csv(index=False).encode('utf-8')
                        zipf.writestr(f"{col}_{safe_val}.csv", csv_data)
                zip_buffer.seek(0)
                add_log(f"Split {uploaded_file.name} into {len(groups)} groups by column {col}.")
                st.success(f"Split into {len(groups)} files.")
                st.download_button("Download ZIP", data=zip_buffer, file_name="split_by_column.zip", mime="application/zip")