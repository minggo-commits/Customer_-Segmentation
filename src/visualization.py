import matplotlib.pyplot as plt

def plot_clusters(reduced, labels):
    fig, ax = plt.subplots(figsize=(8, 5))
    scatter = ax.scatter(reduced[:, 0], reduced[:, 1], c=labels, cmap="viridis")
    ax.set_title("Visualisasi Customer Clusters")
    ax.set_xlabel("PCA 1")
    ax.set_ylabel("PCA 2")
    return fig
