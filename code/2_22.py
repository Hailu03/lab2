from pandas.plotting import andrews_curves
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('iris')

# Create an Andrews curves plot
plt.title('Andrews curves for Iris Flower Types')
andrews_curves(data, 'species', colormap=plt.get_cmap("Set2"))
plt.show()