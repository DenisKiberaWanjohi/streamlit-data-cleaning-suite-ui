import streamlit as st
import pandas as pd
import io
from utils.logger import add_log

def run_combine_tool():
    st.header("📎 Combine Files")
    st.write("Upload multiple CSV or Excel files to combine them into a single dataset.")

    uploaded_files = st.file_uploader("Upload files:", type=['csv', 'xlsx'], accept_multiple_files=True)
    add_source_col = st.checkbox("Add source filename as a column", value=True)
    align_schemas = st.checkbox("Align schemas (outer join on columns)", value=True)

    if uploaded_files and st.button("Combine Files"):
        dfs = []
        for file in uploaded_files:
            filename = file.name
            if filename.endswith('.csv'):
                df = pd.read_csv(file)
                if add_source_col:
                    df['SourceFile'] = filename
                dfs.append(df)
            elif filename.endswith('.xlsx'):
                excel = pd.ExcelFile(file)
                sheets_to_collect = {'bom': [], 'supplier': [], 'contact': []}
                for sheet_name in excel.sheet_names:
                    lower_sheet = sheet_name.lower()
                    for category in sheets_to_collect.keys():
                        if category in lower_sheet:
                            df = excel.parse(sheet_name)
                            if add_source_col:
                                df['SourceFile'] = f"{filename}::{sheet_name}"
                            sheets_to_collect[category].append(df)

                for cat, dfs_list in sheets_to_collect.items():
                    if dfs_list:
                        dfs.append(pd.concat(dfs_list, ignore_index=True))

        if not dfs:
            st.warning("No valid sheets or CSV files found.")
            return

        if align_schemas:
            combined = pd.concat(dfs, ignore_index=True, sort=False)
        else:
            common_cols = set(dfs[0].columns)
            for df in dfs[1:]:
                common_cols.intersection_update(set(df.columns))
            combined = pd.concat([df[list(common_cols)] for df in dfs], ignore_index=True)

        add_log(f"Combined {len(uploaded_files)} files into one DataFrame with {combined.shape[0]} rows.")
        st.success("Files combined successfully!")
        st.dataframe(combined.head(20))

        csv = combined.to_csv(index=False).encode('utf-8')
        st.download_button("Download Combined CSV", data=csv, file_name="combined_output.csv", mime="text/csv")

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            combined.to_excel(writer, index=False, sheet_name="Combined")
        buffer.seek(0)
        st.download_button("Download Combined Excel", data=buffer, file_name="combined_output.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")