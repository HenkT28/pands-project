# Henk Tjalsma, 2019
# Iris Data Set - plotting iris data set

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# https://etav.github.io/python/pairs_plot_python_seaborn.html

# Importing libraries
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Set styling preferences
sns.set(font_scale=1.35, style="ticks") 

# Reading Iris Dataset in Pandas Dataframe
# data = pd.read_csv("iris_original.csv")
# names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']

iris = sns.load_dataset("iris")

# Getting error - https://stackoverflow.com/a/54732522 (using a non-tuple sequence for multidimensional indexing is deprecated)
# pip install --user --upgrade scipy
plot = sns.pairplot(iris, hue='species', diag_kind="kde", palette='husl')

plt.show()