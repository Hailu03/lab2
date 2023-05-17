import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")

plt.figure(figsize=(10, 5))
plt.title("Iris Species Density")
plt.xlabel("Length")
plt.ylabel("Density")
sns.kdeplot(data=iris,fill=True,alpha=0.5, linewidth=0.5)
plt.show()