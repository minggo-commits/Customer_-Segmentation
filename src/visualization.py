import matplotlib.pyplot as plt

def plot_clusters(reduced, labels):
    fig, ax = plt.subplots(figsize=(8, 5))
    scatter = ax.scatter(reduced[:, 0], reduced[:, 1], c=labels, cmap="viridis", alpha=0.7)
    legend1 = ax.legend(*scatter.legend_elements(), title="Cluster")
    ax.add_artist(legend1)
    ax.set_title("Visualisasi Customer Clusters")
    ax.set_xlabel("PCA 1")
    ax.set_ylabel("PCA 2")
    return fig
