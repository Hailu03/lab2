import itertools
import numpy as np
import matplotlib.pyplot as plt

# load iris from numpy
iris = np.genfromtxt('iris.data', delimiter=',', dtype=None, encoding=None)
iris = np.array([list(x) for x in iris])

features = iris[:, 0:4]
features = features.astype(np.float64)

# Calculate the mean and standard deviation for each feature
mean_values = np.mean(features, axis=0)
std_values = np.std(features, axis=0)

# Set the labels for the x-axis
labels = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth']

# Plot the deviation chart
plt.figure(figsize=(10, 6))
plt.errorbar(labels, mean_values, yerr=std_values, fmt='o', capsize=5)

# Set the title and labels
plt.title('Deviation Chart for Iris Flower Types')
plt.xlabel('Features')
plt.ylabel('Values')

# Show the plot
plt.show()
