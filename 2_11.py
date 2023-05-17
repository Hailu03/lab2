import numpy as np
import matplotlib.pyplot as plt

# load iris from numpy
iris = np.genfromtxt('iris.data', delimiter=',', dtype=None, encoding=None)
iris = np.array([list(x) for x in iris])

flower_features = ["sepalLength", "sepalWidth", "petalLength", "petalWidth"]
features = iris[:,0:4]
features = features.astype(np.float64)
setosa = features[0:50]
versicolor = features[50:100]
virginica = features[100:150]

labels = ["setosa", "versicolor", "virginica"]
flowers = [setosa, versicolor, virginica]

def box_chart(flower, index):
    # box chart for each feature for all the flower
    data = []
    for i in range(4):
        data.append(flower[:,i])

    plt.figure(figsize=(15,8))
    plt.boxplot(data, labels=flower_features, patch_artist=True, medianprops={'linewidth':2})
    plt.xlabel("Features")
    plt.ylabel("cm")

    plt.title("Boxplot of iris flower features for " + labels[index] + " flower")
    plt.show()

for i in range(3):
    box_chart(flowers[i], i)

