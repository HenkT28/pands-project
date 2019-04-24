# Henk Tjalsma, 2019
# Iris Data Set - plotting iris data set

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# https://stackoverflow.com/a/45721331
# https://mclguide.readthedocs.io/en/latest/sklearn/moreex1.html

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# Loading iris data set - https://scikit-learn.org/stable/datasets/index.html
iris= load_iris()

colors= ['blue', 'red', 'green']

# https://github.com/PyCQA/pylint/issues/1161 - hitting error -> Instance of 'tuple' has no 'data' memberpylint(no-member), but script works ok. 
for feature in range(iris.data.shape[1]): # (shape = 150, 4)
    plt.subplot(2, 2, feature+1) # subplot starts from 1 (not 0)
    for label, color in zip(range(len(iris.target_names)), colors):
        # find the label and plot the corresponding data
        plt.hist(iris.data[iris.target==label, feature],
                 label=iris.target_names[label],
                 color=color)
    plt.xlabel(iris.feature_names[feature])
    plt.legend()
plt.show()
