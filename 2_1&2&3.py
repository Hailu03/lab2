import numpy as np
import matplotlib.pyplot as plt

# load iris from numpy
iris = np.genfromtxt('iris.data', delimiter=',', dtype=None, encoding=None)
iris = np.array([list(x) for x in iris])

# convert categorical data to numerical data
labels = np.unique(iris[:, 4])
iris[:,4] = np.array([np.where(labels == x)[0][0] for x in iris[:, 4]])
iris = iris.astype(np.float64)

# divide into features and labels
X = iris[:, 0:4]
y = iris[:, 4] 
print()

#max
max = np.max(X,axis=0)
print("Max for all flower type: ", max)

#min
min = np.min(X,axis=0)
print("Min for all flower type: ", min)

# mean
mean = np.mean(X,axis=0)
print("Mean for all flower type: ", mean)

# standard deviation
std = np.std(X,axis=0)
print("Standard deviation for all flower type: ", std)

# variance
var = np.var(X,axis=0)
print("Variance for all flower type: ", var)

# median
median = np.median(X,axis=0)
print("Median for all flower type: ", median)

# 25% percentile
q1 = np.percentile(X, 25,axis=0)
print("25% percentile for all flower type: ", q1)

# 75% percentile
q2 = np.percentile(X, 75,axis=0)
print("75% percentile for all flower type: ", q2)

# set width of bar
barWidth = 0.1
fig = plt.subplots(figsize =(12, 8))

# set position of bar on X axis
br1 = np.arange(len(max))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]
br5 = [x + barWidth for x in br4]
br6 = [x + barWidth for x in br5]
br7 = [x + barWidth for x in br6]
br8 = [x + barWidth for x in br7]

# Make the plot
plt.bar(br1, max, color ='r', width = barWidth,
        edgecolor ='grey', label ='max')
plt.bar(br2, min, color ='g', width = barWidth,
        edgecolor ='grey', label ='min')
plt.bar(br3, mean, color ='b', width = barWidth,
        edgecolor ='grey', label ='mean')
plt.bar(br4, std, color ='y', width = barWidth,
        edgecolor ='grey', label ='standard deviation')
plt.bar(br5, var, color ='c', width = barWidth,
        edgecolor ='grey', label ='variance')
plt.bar(br6, median, color ='m', width = barWidth,
        edgecolor ='grey', label ='median')
plt.bar(br7, q1, color ='k', width = barWidth,
        edgecolor ='grey', label ='25% percentile')
plt.bar(br8, q2, color ='w', width = barWidth,
        edgecolor ='grey', label ='75% percentile')

# Adding Xticks
plt.xlabel('Flower features', fontweight ='bold', fontsize = 15)
plt.ylabel('Values', fontweight ='bold', fontsize = 15)
plt.xticks([r + 0.4 for r in range(len(max))],
        ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth'])

plt.legend()
plt.show()