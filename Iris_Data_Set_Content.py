# Henk Tjalsma, 2019
# Iris Data Set - plotting iris data set

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Importing Package 
import numpy
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Reading Iris Dataset in Pandas Dataframe
data = pandas.read_csv("iris_original.csv")
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']

# Printing DataFrame - only first 30 rows to understand what data look like
# Data has 5 Columns - first four are features and fifth is Classfication of the Iris type
# print(data.head(30))

# https://stackoverflow.com/a/52281061 -> select first 3 Rows With Distinct Values in Specific Column "species"
print(data.drop_duplicates(['species']).groupby('species').head(3))

