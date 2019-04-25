# Henk Tjalsma, 2019
# Iris Data Set - plotting iris data set

# https://www.kaggle.com/lnbalon/iris-dataset-eda-and-classification-analysis

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

# Reading Iris Dataset in Pandas Dataframe
iris = pd.read_csv("iris_original.csv")
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# The boxplot feature of seaborn is very useful to look at individual features
# This is combined with Seaborn's striplot function  - it adds a layer of individual points
# https://seaborn.pydata.org/generated/seaborn.stripplot.html
# Setting jitter=True ensures that not all points fall on the same line
# Saving the resulting axes as ax each time causes the resulting plot to be shown
ax = sns.boxplot(x="species", y="petal_length", data=iris)
ax = sns.stripplot(x="species", y="petal_length", data=iris, jitter=True, edgecolor="gray")
plt.show()

ax = sns.boxplot(x="species", y="petal_width", data=iris)
ax = sns.stripplot(x="species", y="petal_width", data=iris, jitter=True, edgecolor="gray")
plt.show()

ax = sns.boxplot(x="species", y="sepal_length", data=iris)
ax = sns.stripplot(x="species", y="sepal_length", data=iris, jitter=True, edgecolor="gray")
plt.show()

ax = sns.boxplot(x="species", y="sepal_width", data=iris)
ax = sns.stripplot(x="species", y="sepal_width", data=iris, jitter=True, edgecolor="gray")
plt.show()