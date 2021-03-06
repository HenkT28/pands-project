# Henk Tjalsma, 2019
# Iris Data Set - 3D graph iris data set

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Importing libraries
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Reading Iris Dataset in Pandas Dataframe
data = pd.read_csv("iris_original.csv")
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# https://stackoverflow.com/questions/38666527/what-is-the-necessity-of-plt-figure-in-matplotlib
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

x=data["sepal_length"]
y=data["petal_length"]
z=data["petal_width"]

color=("Iris-setosa", "Iris-virginica", "Iris-versicolor")
color=['Iris-setosa', 'Iris-virginica', 'Iris-versicolor']
ax.scatter(x,y,z,c='r',marker='o')

ax.set_xlabel('sepal_length')
ax.set_ylabel('petal_length')
ax.set_zlabel('petal_width')

plt.show()
