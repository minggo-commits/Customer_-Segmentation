import pandas as pd

def load_file(uploaded_file):
    """Load file CSV/XLS"""
    if uploaded_file.name.endswith("csv"):
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_excel(uploaded_file)
