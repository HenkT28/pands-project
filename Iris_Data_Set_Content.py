# Henk Tjalsma, 2019
# Iris Data Set - content

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Importing Package 
import numpy
import pandas

# Reading Iris Dataset in Pandas Dataframe
data = pandas.read_csv("iris_original.csv")
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Printing DataFrame - only first 30 rows to understand what data look like
# Data has 5 Columns - first four are features and fifth is classfication
# print(data.head(30))

# https://stackoverflow.com/a/52281061 -> select first 3 Rows With Distinct Values in Specific Column "species"
print(data.drop_duplicates(['species']).groupby('species').head(3))

