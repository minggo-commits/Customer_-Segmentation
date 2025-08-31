from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd

def run_kmeans(df, X_scaled, features, k):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    df["Cluster"] = labels

    pca = PCA(n_components=2)
    reduced = pca.fit_transform(X_scaled)

    summary = df.groupby("Cluster")[features].mean()

    return df, summary, reduced, labels
