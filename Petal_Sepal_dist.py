# Henk Tjalsma, 2019
# Iris Data Set - petal and sepal distibution

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Importing Packages 
import numpy
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Reading Iris Dataset in Pandas Dataframe
data = pandas.read_csv("iris_original.csv")
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

setosa=data[data['species']=='setosa']
versicolor =data[data['species']=='versicolor']
virginica =data[data['species']=='virginica']

# https://stackoverflow.com/questions/38666527/what-is-the-necessity-of-plt-figure-in-matplotlib
plt.figure()
# Adding multiple Axes objects  
fig,ax=plt.subplots(1,2,figsize=(18, 10))

setosa.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal_length", y="sepal_width", kind="scatter", ax=ax[0], label='virginica', color='g')

setosa.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="petal_length", y="petal_width", kind="scatter", ax=ax[1], label='virginica', color='g')

# Setting title of the graphs
ax[0].set(title='Sepal Comparison', ylabel='sepal_width')
ax[1].set(title='Petal Comparison',  ylabel='petal_width')
ax[0].legend()
ax[1].legend()
plt.show()
# plt.close()