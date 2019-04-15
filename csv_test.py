# https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/

# Load the Pandas libraries with alias 'pd'
import pandas as pd

# Load data from csv file - in the same directory that your python process is based
# Control delimiters, rows, column names with read_csv 

# https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/

# https://www.geeksforgeeks.org/different-ways-to-import-csv-file-in-pandas/

# making data frame   
iris = pd.read_csv('iris_original.csv')   
    
# print(iris.head())     

# https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn

print(iris.columns)