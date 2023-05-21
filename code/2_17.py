import itertools
import numpy as np
import matplotlib.pyplot as plt

# load iris from numpy
iris = np.genfromtxt('iris.data', delimiter=',', dtype=None, encoding=None)
iris = np.array([list(x) for x in iris])

flower_features = ["sepalLength", "sepalWidth", "petalLength", "petalWidth"]

features = iris[:,0:4]
features = features.astype(np.float64)
color = ['purple', 'green', 'brown', 'orange', 'red', 'pink']

setosa = features[0:50]
versicolor = features[50:100]
virginica = features[100:150]

labels = ["setosa", "versicolor", "virginica"]
flowers = [setosa, versicolor, virginica]

def plot_histogram(flower, index):
    i = 0
    # Scatter plot for each column
    fig = plt.figure(figsize=(16,8))
    for col_a, col_b in itertools.combinations([0,1,2,3], 2):
        x = flower[:,col_a]
        y = flower[:,col_b]
        plt.subplot(2,3,i+1)
        plt.scatter(x,y,s=flower[:,3]*100,color=color[index],alpha=0.5)
        plt.title(f"Bubble plot of {flower_features[col_a]} vs {flower_features[col_b]} for {labels[index]}")
        plt.xlabel(flower_features[col_a],color="blue")
        plt.ylabel(flower_features[col_b],color="blue")
        plt.tight_layout()

        i += 1
    plt.show()

for i in range(len(flowers)):
    plot_histogram(flowers[i], i)