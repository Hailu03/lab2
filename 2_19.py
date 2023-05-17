import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")

setosa = iris[iris["species"] == "setosa"]
versicolor = iris[iris["species"] == "versicolor"]
virginica = iris[iris["species"] == "virginica"]

labels = ["setosa", "versicolor", "virginica"]
flowers = [setosa, versicolor, virginica]

def plot(flower, index):
    sns.kdeplot(data=flower, fill=True, alpha=0.5, linewidth=0.5)
    plt.title(f"Iris Species Density for {labels[index]}")
    plt.xlabel("Length")
    plt.ylabel("Density")
    plt.show()

for i in range(len(flowers)):
    plot(flowers[i], i)