# Henk Tjalsma, 2019
# Iris Data Set - plotting iris data set

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# https://stackoverflow.com/a/45721331

import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd

# Loading iris data set - https://scikit-learn.org/stable/datasets/index.html
iris= datasets.load_iris()

fig, axes = plt.subplots(nrows= 2, ncols=2)
colors= ['blue', 'red', 'green']

# https://github.com/PyCQA/pylint/issues/1161 - hitting error -> Instance of 'tuple' has no 'data' memberpylint(no-member), but script works ok. 
for i, ax in enumerate(axes.flat):
    for label, color in zip(range(len(iris.target_names)), colors):
        ax.hist(iris.data[iris.target==label, i], label=             
                            iris.target_names[label], color=color)
        ax.set_xlabel(iris.feature_names[i])  
        ax.legend(loc='upper right')

plt.show()