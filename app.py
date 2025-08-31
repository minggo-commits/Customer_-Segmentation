import streamlit as st
import pandas as pd
from src.preprocessing import preprocess_data
from src.clustering import run_kmeans
from src.visualization import plot_clusters
from src.utils import load_file

st.title("📊 Customer Segmentation Platform")

uploaded_file = st.file_uploader("Upload file CSV/XLS", type=["csv", "xls", "xlsx"])

if uploaded_file:
    df = load_file(uploaded_file)
    st.write("### Data Customer")
    st.dataframe(df.head())

    features = st.multiselect(
        "Pilih fitur untuk clustering:",
        df.columns.tolist(),
        default=df.select_dtypes(include=['int64','float64']).columns.tolist()
    )

    k = st.slider("Jumlah Cluster (k)", 2, 10, 3)

    if st.button("Lakukan Segmentasi"):
        X_scaled, scaler = preprocess_data(df, features)
        df_clustered, summary, reduced, labels = run_kmeans(df, X_scaled, features, k)

        st.write("### Data dengan Cluster")
        st.dataframe(df_clustered.head())

        st.write("### Visualisasi Cluster")
        fig = plot_clusters(reduced, labels)
        st.pyplot(fig)

        st.write("### Ringkasan Cluster")
        st.dataframe(summary)
