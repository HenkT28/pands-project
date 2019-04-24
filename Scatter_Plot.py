# Henk Tjalsma, 2019
# Iris Data Set - plotting iris data set

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Importing libraries
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Reading Iris Dataset in Pandas Dataframe
data = pd.read_csv("iris_original.csv")
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']

# https://www.kaggle.com/anthonyhills/classifying-species-of-iris-flowers
# https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn
# # It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
sns.FacetGrid(data, hue="species", height=10).map(plt.scatter, "sepal_length", "sepal_width").add_legend() 

plt.show()
