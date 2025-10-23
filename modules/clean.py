import streamlit as st
import pandas as pd
import re
import io
from utils.logger import add_log

def run_clean_tool():
    st.header("🧹 Clean Special Characters")
    uploaded_file = st.file_uploader("Upload a CSV or Excel file:", type=["csv", "xlsx"])
    pattern = st.text_input("Regex pattern to remove (default removes most punctuation)", value=r"[^A-Za-z0-9\s]")

    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            sheetname = None
        else:
            sheetname = st.text_input("Sheet name (for Excel)", value="Sheet1")
            try:
                df = pd.read_excel(uploaded_file, sheet_name=sheetname)
            except Exception as e:
                st.error(f"Failed to read Excel sheet: {e}")
                return

        text_columns = df.select_dtypes(include='object').columns.tolist()
        cols_to_clean = st.multiselect("Select columns to clean:", options=text_columns, default=text_columns)

        if st.button("Clean Data"):
            df_cleaned = df.copy()
            for col in cols_to_clean:
                df_cleaned[col] = df_cleaned[col].astype(str).apply(lambda x: re.sub(pattern, '', x))

            st.success("Special characters cleaned.")
            st.dataframe(df_cleaned.head(10))

            summary = []
            for col in cols_to_clean:
                specials = set(re.findall(r'[^A-Za-z0-9\s]', ''.join(df_cleaned[col].dropna().astype(str))))
                summary.append((col, ", ".join(sorted(specials)) if specials else "None"))
            st.subheader("Remaining special characters by column")
            st.dataframe(pd.DataFrame(summary, columns=["Column", "Remaining Special Characters"]))

            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df_cleaned.to_excel(writer, index=False, sheet_name='CleanedData')
                pd.DataFrame(summary, columns=["Column", "Remaining Special Characters"]).to_excel(writer, index=False, sheet_name='Summary')
            output.seek(0)

            add_log(f"Cleaned special characters from {len(cols_to_clean)} columns in {uploaded_file.name}.")
            st.download_button("Download Cleaned Excel", data=output, file_name="cleaned_output.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")