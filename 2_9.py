import numpy as np
import matplotlib.pyplot as plt

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
    # histogram chart for each featuqre for all the flower
    # for i in range(4):
    #     plt.hist(flower[:,i], bins=20, color=color[index])
    #     plt.title(f"histogram of {flower_features[i]} for {labels[index]}")
    #     plt.show()

    # histogram chart for each feature for all the flower
    fig = plt.figure(figsize=(15,8))
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.hist(flower[:,i], bins=20, color=color[i], edgecolor='black', alpha=0.5)
        plt.xlabel(f"{flower_features[i]} cm")
        plt.ylabel("Frequency")

        plt.title(f"histogram of {flower_features[i]} for {labels[index]}")
        plt.tight_layout()

    plt.show()

for i in range(len(flowers)):
    histogram(flowers[i], i)