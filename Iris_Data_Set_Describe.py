# Henk Tjalsma, 2019
# Iris Data Set - describe it

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Importing Package 
import numpy
import pandas

# Reading Iris Dataset in Pandas Dataframe
data = pandas.read_csv("iris_original.csv")
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Created 3 DataFrame for each Species
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
# DataFrame.describe(percentiles=None, include=None, exclude=None)[source]
# Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.

setosa=data[data['species']=='setosa']
versicolor =data[data['species']=='versicolor']
virginica =data[data['species']=='virginica']

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())

# print(data.describe())

