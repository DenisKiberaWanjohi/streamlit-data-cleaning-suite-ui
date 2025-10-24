# Data Cleaning Suite

## Overview
**Data Cleaning Suite** is a Streamlit-based web application designed for teams to automate repetitive data preparation tasks, where members often use their own methods to clean and prep data, which can be time-consuming. The app provides an intuitive dashboard with three primary tools for data analysts and engineers: combining multiple files, splitting large files, and cleaning special characters in text data. The interface is designed for ease of use, featuring a sidebar for navigation and a clean dashboard displaying the three tools as card-style panes. Users can upload Excel or CSV files, preview data, apply transformations, and download the results without writing any code. This application is ideal for standardizing team workflows, quickly merging datasets, breaking down large files, or cleaning and standardizing text fields across multiple datasets.

##UI link
https://data-cleaning-suite-ui.streamlit.app/

## Features
- **Combine Files:** Merge multiple Excel or CSV files into one consolidated file. Supports:
  - Merging files with multiple sheets (e.g., sheets containing **BOM details**, **Supplier details**, **Contact details**) and combining data across files.
  - Option to add a "Source Filename" column for row traceability.
  - Supports both Excel (.xls/.xlsx) and CSV files.

- **Split File:** Divide a large dataset into smaller chunks.
  - **By Row Count:** Split a file into parts with a specified number of rows.
  - **By Unique Values:** Split a file by unique values in a selected column.
  - Outputs are zipped for convenient download.

- **Clean Special Characters:** Remove or replace unwanted characters in text columns.
  - Upload Excel or CSV, select columns, define unwanted characters or regex patterns.
  - Provides a summary of remaining special characters.
  - Outputs cleaned data in Excel or CSV format, including a Summary sheet if applicable.

- **User Interface:**
  - Dashboard with three equal-height card-style panes for each tool.
  - Sidebar navigation to Dashboard, Logs, and Support pages.
  - File upload, preview, configuration options, and download buttons for each tool.

---

## Usage Instructions

### Running the App Locally
Once the app is running, your web browser will open at `http://localhost:8501`. Use the sidebar to navigate between **Dashboard**, **Logs**, and **Support**.

### Dashboard (Selecting a Tool)
- Click on one of the tool cards: **Combine Files**, **Split File**, or **Clean Special Characters**.  
- Follow the on-screen instructions to upload files and configure options.

### Combine Files Tool
1. Upload two or more CSV or Excel files.  
2. (Optional) Add a "Source Filename" column.  
3. Click **Combine** to merge files.  
4. Download the combined result as CSV or Excel.

### Split File Tool
1. Upload a CSV or Excel file.  
2. Choose a split method:
   - **By Row Count:** Define number of rows per chunk.  
   - **By Column Value:** Select a column to split by unique values.  
3. Click **Split** to generate multiple files.  
4. Download a ZIP containing all split files.

### Clean Special Characters Tool
1. Upload a CSV or Excel file.  
2. Select the columns to clean.  
3. Specify regex pattern (or use a preset).  
4. Click **Clean** to remove/replace unwanted characters.  
5. Preview the cleaned data and summary of remaining special characters.  
6. Download the cleaned dataset (Excel or CSV).


## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository** and create a new branch for your feature or bugfix.  
2. **Write clear commit messages** and test your changes thoroughly.  
3. **Maintain UI consistency**, keeping dashboard styling and layout intact.  
4. Submit a **Pull Request** with a description of your changes.  
5. Optionally, **report issues** or request new features via GitHub Issues.  

> By contributing, you agree to follow the project’s code of conduct and maintain a collaborative, professional environment.
