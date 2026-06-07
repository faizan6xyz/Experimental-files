import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
# sns.load_dataset("iris")
# sns.load_dataset("titanic")
# sns.load_dataset("penguins")
# sns.load_dataset("flights")
# these are the dataset which comes with the seaborn 
data = sns.load_dataset("tips")
print(data.head())
# Shows relationship between two variables.
sns.scatterplot(x="total_bill", y="tip", data=data)
plt.title("Scatter Plot")
plt.show()
# Shows trends.
sns.lineplot(x="total_bill", y="tip", data=data)
plt.title("Line Plot")
plt.show()
# Shows category comparison.
sns.barplot(x="day", y="total_bill", data=data)
plt.title("Bar Plot")
plt.show()
# Counts categorical values.
sns.barplot(x="day", y="total_bill", data=data)
plt.title("Bar Plot")
plt.show()
# Shows distribution of values.
sns.histplot(data["total_bill"], bins=10)
plt.title("Histogram")
plt.show()
# Shows spread and outliers.
sns.boxplot(x="day", y="total_bill", data=data)
plt.title("Box Plot")
plt.show()
# Shows distribution + density.
sns.violinplot(x="day", y="total_bill", data=data)
plt.title("Violin Plot")
plt.show()
# shows correlation
corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Heatmap")
plt.show()
# Shows relationships between all numerical variables.
sns.pairplot(data)
plt.show()
# Shows distribution of categorical data.
sns.stripplot(x="day", y="total_bill", data=data)
plt.title("Strip Plot")
plt.show()
# Similar to strip plot but avoids overlap.
sns.swarmplot(x="day", y="total_bill", data=data)
plt.title("Swarm Plot")
plt.show()