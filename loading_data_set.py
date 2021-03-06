# https://plot.ly/ipython-notebooks/principal-component-analysis/

import pandas as pd

df = pd.read_csv(
    filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', 
    header=None, 
    sep=',')

df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
# drops the empty line at file-end
df.dropna(how="all", inplace=True) 

df.tail()