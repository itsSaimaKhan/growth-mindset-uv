import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title=" File Converter & Cleaner", layout="wide")
st.title("File Converter & Cleaner")
st.write("Upload Your CSV and Excel Files to clean the data convert formats effortlessly")

files = st.file_uploader("Upload CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1]
        
        data.pdf.csv

