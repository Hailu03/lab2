import itertools
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

def plot_correlation(flower,index):
    correlation = {}

    for col_a, col_b in itertools.combinations([0,1,2,3], 2):
        x = flower[col_a]
        y = flower[col_b]

        xy = np.mean(x*y)
        mean_x = np.mean(x)
        mean_y = np.mean(y)
        var_x = np.var(x)
        var_y = np.var(y)
        corr = (xy-mean_x*mean_y)/ np.sqrt(var_x*var_y)

        correlation[f"{flower_features[col_a]}_{flower_features[col_b]}"] = corr

    print(f"Correlation for {labels[index]}: ")
    print(correlation)

for i in range(len(flowers)):
    plot_correlation(flowers[i],i)
    print("\n")
