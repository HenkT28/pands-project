# https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn
# https://medium.com/@neuralnets/data-visualization-with-python-and-seaborn-part-1-29c9478a8700

# https://stackoverflow.com/a/49404781

# https://www.tutorialspoint.com/seaborn/seaborn_importing_datasets_and_libraries.htm

# Pandas for managing datasets
import pandas as pd

# Matplotlib for additional customization
from matplotlib import pyplot as plt

# Seaborn for plotting and styling
import seaborn as sns
df = sns.load_dataset("iris")
print(df.head())
