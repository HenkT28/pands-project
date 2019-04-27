# Henk Tjalsma, 2019
# Iris Data Set - minimum value of each column
# Removed headers csv file otherwise generates error "nan" -> not a number, it means the csv file contained column headers

# https://www.dataquest.io/blog/numpy-tutorial-python/

# Using numpy package to calculate the minimum value of each column
import numpy as np

# https://stackoverflow.com/a/3519314
# https://janakiev.com/blog/csv-in-python/
# Read the csv file into an array.
my_data_set = np.genfromtxt('iris.csv', delimiter=',')

# All of the values in the 1st column of the array
# firstcolumn = (my_data_set[:,0]) 
# Used min function numpy package this time
min_firstcolumn = np.min(my_data_set[:,0]) 

# All of the values in the 2nd column of the array
# secondcolumn = (my_data_set[:,1])
min_secondcolumn = np.min(my_data_set[:,1])

# All of the values in the 3rd column of the array
# thirdcolumn = (my_data_set[:,2])
min_thirdcolumn = np.min(my_data_set[:,2])

# All of the values in the 4th column of the array
# fourthcolumn = (my_data_set[:,3])
min_fourthcolumn = np.min(my_data_set[:,3])

# print("The output of 1st column is: ",firstcolumn)
# print("The output of 2nd column is: ",secondcolumn)
# print("The output of 3rd column is: ",thirdcolumn)
# print("The output of 4th column is: ",fourthcolumn)

print("The minimum value of 1st column is: ",min_firstcolumn)
print("The minimum value of 2nd column is: ",min_secondcolumn)
print("The minimum value of 3rd column is: ",min_thirdcolumn)
print("The minimum value of 4th column is: ",min_fourthcolumn)
