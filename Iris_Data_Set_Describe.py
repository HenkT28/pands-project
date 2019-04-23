# Henk Tjalsma, 2019
# Iris Data Set - plotting iris data set

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Importing Package 
import sys
import numpy
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings

# Reading Iris Dataset in Pandas Dataframe
data = pandas.read_csv("iris_original.csv")
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']

# Created 3 DataFrame for each Species

setosa=data[data['species']=='setosa']
versicolor =data[data['species']=='versicolor']
virginica =data[data['species']=='virginica']

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())

