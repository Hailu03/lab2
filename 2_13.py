import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load iris from numpy
iris = np.genfromtxt('iris.data', delimiter=',', dtype=None, encoding=None)
iris = np.array([list(x) for x in iris])

color = ['pink', 'purple', 'yellow', 'orange']
flower_features = ["sepalLength", "sepalWidth", "petalLength", "petalWidth"]
features = iris[:,0:4]
features = features.astype(np.float64)

setosa = features[0:50]
versicolor = features[50:100]
virginica = features[100:150]
labels = ["setosa", "versicolor", "virginica"]
flowers = [setosa, versicolor, virginica]

def histogram(flower, index):
    # histogram chart for each feature for all the flower
    fig, axes = plt.subplots(2, 2, figsize=(15, 8))
    for i, ax in enumerate(axes.flat):
        sns.histplot(flower[:, i], bins=20, color=color[i], edgecolor='black', alpha=0.5, ax=ax)
        sns.kdeplot(flower[:, i], color='blue', fill=True, alpha=0.3, ax=ax)
        ax.set_xlabel(f"{flower_features[i]} cm")
        ax.set_ylabel("Frequency")
        ax.set_title(f"Distribution of {flower_features[i]} for {labels[index]}")
        ax.legend()
    plt.tight_layout()

    plt.show()

for i in range(len(flowers)):
    histogram(flowers[i], i)