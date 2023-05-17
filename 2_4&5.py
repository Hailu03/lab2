import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# load iris from numpy
iris = np.genfromtxt('iris.data', delimiter=',', dtype=None, encoding=None)
iris = np.array([list(x) for x in iris])

features = iris[:,0:4]
features = features.astype(np.float64)

setosa = features[0:50]
versicolor = features[50:100]
virginica = features[100:150]

labels = ["setosa", "versicolor", "virginica"]
flowers = [setosa, versicolor, virginica]

def compute(flower,index):
    #max
    max = np.max(flower,axis=0)
    print("Max for all flower type: ", max)

    #min
    min = np.min(flower,axis=0)
    print("Min for all flower type: ", min)

    # mean
    mean = np.mean(flower,axis=0)
    print("Mean for all flower type: ", mean)

    # standard deviation
    std = np.std(flower,axis=0)
    print("Standard deviation for all flower type: ", std)

    # variance
    var = np.var(flower,axis=0)
    print("Variance for all flower type: ", var)

    # median
    median = np.median(flower,axis=0)
    print("Median for all flower type: ", median)

    # 25% percentile
    q1 = np.percentile(flower, 25,axis=0)
    print("25% percentile for all flower type: ", q1)


    # 75% percentile
    q2 = np.percentile(flower, 75,axis=0)
    print("75% percentile for all flower type: ", q2)

    # set width of bar
    barWidth = 0.1
    # plt.subplots(figsize =(12, 8))
    plt.subplot(1, 3, i+1)

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
    plt.xlabel(labels[i], fontweight ='bold', fontsize = 10)
    plt.ylabel('Values', fontweight ='bold', fontsize = 10)
    plt.xticks([r + 0.4 for r in range(len(max))],
            ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth'])

    plt.legend()

fig = plt.figure(figsize=(19,10))
SMALL_SIZE = 7
plt.rc('font', size=SMALL_SIZE)
for i in range(len(flowers)):
    compute(flowers[i],i)
plt.show()