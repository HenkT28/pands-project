# Project 2019 - Programming and Scripting

This readme contains background info, instructions, and research into the well-known Fisher’s Iris data set, for Programming and Scripting module (GMIT H.Dip Data Analytics - Academic Year 2019 - 2020).

1. Research background information about the data set and write a summary about it.

2. Keep a list of references you used in completing the project.

3. Download the data set and write some Python code to investigate it.

4. Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set. A Python script will quickly do this for you.

5. Write a summary of your investigations.

6. Include supporting tables and graphics as you deem necessary.


Student: Henk Tjalsma

GMIT email address: G00376321@gmit.ie


## Problem statement
The project entails researching the data set, and then writing documentation and code in the Python programming language based on that research.

1. Go to Github web site - User Account: HenkT28 

(https://github.com/HenkT28)

2. Click on the download button, and copy/paste the link:

https://github.com/HenkT28/pands-project.git


## Background - Fisher’s Iris data set

Below is taken from the wikipedia page, Iris Flower Data Set: 

https://en.wikipedia.org/wiki/Iris_flower_data_set [19]

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper:

* The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[1] 


It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.[2] 

Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".[3]

The Gaspésie, or Gaspé Peninsula, the Gaspé or Gaspesia, is a peninsula along the south shore of the Saint Lawrence River to the east of the Matapedia Valley in Quebec, Canada, that extends into the Gulf of Saint Lawrence.


The data set consists of 50 samples from each of three species of Iris (Iris Setosa, Iris Virginica and Iris Versicolor). 

Photo's Iris flowers of the three related species:

![iris_class](https://github.com/HenkT28/pands-project/blob/master/Images/iris_class.png)

The dataset is a record of feature measurements (petal lengths and widths, sepal lengths and widths) of the different species of Iris flowers.[9]

There are five columns in this dataset with the following variable names: Sepal Length, Sepal Width, Petal Length, Petal Width, and Species. The first four variables are real measurements made in centimeters. 

But what are these measurements? And why are these parts of the flower so important? It turns out that this dataset was used to try to make a computer predict which specimens (in rows) belonged to each species of Iris flower. This sort of problem was up in the air in the time before genetics was used to classify animals. At the time, scientists depended on what these species looked like in order to make the distinctions.


Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. Based on the model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.[4]


What are exactly the petals and the sepals of a flower? See below.

![Parts of the Flower](https://github.com/HenkT28/pands-project/blob/master/Images/Parts_of_the_flower.png)

Here’s a rough and simple-worded way of differentiating them:

* Petals — the often vibrantly colored fans that cover the inner part of the flower.

* Sepals — the often green fan base that serves as a cup for the flower to sit on.


## What aspects of the Iris Data Set, make it so successful as an example teaching test data set?

The Iris dataset is deservedly widely used throughout statistical science, especially for illustrating various problems in statistical graphics, multivariate statistics and machine learning.[8]

[a] Containing 150 observations, it is small but not trivial. The dataset contains records under five attributes - petal length, petal width, sepal length, sepal width and species.

There are no null values in the data set.

There are 50 observations of each species (setosa, versicolor, virginica).

Anderson classified 50 examples of 3 different species. Each specimen was [23]:

* Collected on the same day

* Collected by the same person

* Measured using the same instruments

[b] The task it poses of discriminating between three species of Iris from measurements of their petals and sepals is simple but challenging.

[c] The data are real data, but apparently of good quality. In principle and in practice, test datasets could be synthetic and that might be necessary or useful to make a point. Nevertheless, few people object to real data.

[d] The data were used by the celebrated British statistician Ronald Fisher in 1936. The data were originally published by the statistically-minded botanist Edgar S. Anderson, but that earlier origin does not diminish the association.

[e] Using a few famous datasets is one of the traditions we hand down, such as telling each new generation that Student worked for Guinness or that many famous statisticians fell out with each other. That may sound like inertia, but in comparing methods old and new, and in evaluating any method, it is often considered helpful to try them out on known datasets, thus maintaining some continuity in how we assess methods.

[f] Last, but not least, the Iris dataset can be enjoyably coupled with pictures of the flowers concerned, as from e.g. the useful Wikipedia entry on the dataset.


Note:

* Iris setosa, Iris versicolor and Iris virginica are three species (not varieties, as in some statistical accounts); their binominals should be presented in italic, as here; and Iris as genus name and the other names indicating particular species should begin with upper and lower case respectively.


Here is some Python code that defines how this data set can be analyzed:

![Some lines showing how Python can be used](https://github.com/HenkT28/pands-project/blob/master/Images/Some_lines_how_Python_works.png)


And some random examples of plotting the three species, of Iris, against each other:

![Iris Dataset Scatterplot](https://github.com/HenkT28/pands-project/blob/master/Images/Iris_dataset_scatterplot.svg.png)


![Spectramap Biplot Iris Flower Data Set](https://github.com/HenkT28/pands-project/blob/master/Images/Spectramap_Biplot_Iris_Flower_Data_Set_FULL.jpg)


### Python Packages used for analyzing this Iris Data Set

[1]. Pandas/Numpy (also for reading in csv file):

https://pandas.pydata.org/

[2]. Matplotlib & Pyplot:

https://matplotlib.org/

https://matplotlib.org/api/pyplot_api.html

[3]. Seaborn:

https://seaborn.pydata.org/

For example:

https://seaborn.pydata.org/examples/scatterplot_matrix.html

https://seaborn.pydata.org/generated/seaborn.stripplot.html

https://seaborn.pydata.org/generated/seaborn.boxplot.html

[4]. Sklearn:

https://scikit-learn.org/

Sklearn is a machine learning python library that is widely used for data-science related tasks. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means, KNN, etc. Under sklearn you have a library called datasets in which you have multiple datasets that can be used for different tasks including the Iris dataset, all these datasets can be loaded out of the box.

[5]. mpl_toolkits:

https://matplotlib.org/mpl_toolkits/index.html

mpl_toolkits.mplot3d provides some basic 3D plotting (scatter, surf, line, mesh) tools. Not the fastest or most feature complete 3D library out there, but it ships with Matplotlib and thus may be a lighter weight solution for some use cases.


## Below what each script does

1. Iris_Data_Set_Content.py:

First of all I'm reading Iris Dataset in Pandas Dataframe, and although print(data.head(30)) provides a glimpse how the first 30 rows look like, they all refer to the Iris Setosa.

So this script shows 3 Rows With Distinct Values in Specific Column "species", for Iris Setosa, Versicolor, and Virginica.

![Iris_Data_Set_Content_script](https://github.com/HenkT28/pands-project/blob/master/Images/Iris_Data_Set_Content_script.png)

2. Iris_Max_Value.py:

Read the data set, iris.csv file, into an array using numpy library. Then used max function numpy, to retrieve the maximum value for each of the four columns.

![max](https://github.com/HenkT28/pands-project/blob/master/Images/max.png)

3. Iris_Min_Value.py:

Used numpy library, and read the Iris data set, iris.csv into an array. This time I used min function, to retrieve the minimum value for each of the four columns.

![min](https://github.com/HenkT28/pands-project/blob/master/Images/min.png)

4. Iris_Mean_Value.py:

I read the data set, iris.csv file into an array and used mean function numpy, to get the mean value for each of the four columns. Just note using numpy package to calculate the mean, is not the same as average, of each column.

![mean](https://github.com/HenkT28/pands-project/blob/master/Images/mean.png)

5. Iris_Data_Set_Describe.py:

First of all I'm reading Iris Dataset in Pandas Dataframe, then created 3 DataFrame for each Species and used describe function, to generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.

The first section describes "Setosa", the second part "Versicolor", and the third section "Virginica".

![Describe](https://github.com/HenkT28/pands-project/blob/master/Images/Describe.png)

For numeric data, as in this case, the result’s index will include count, mean, std, min, max as well as lower, 50 and upper percentiles. By default the lower percentile is 25 and the upper percentile is 75. The 50 percentile is the same as the median.

The percentiles to include in the output. All should fall between 0 and 1. 

These are some parametric and non parametric statistics of our dataset. 

Parametric: mean, std, min, max, count. Non Parametric: 25%, 50%, 75%.

Running print(data.describe()) produces below summary:

![summary](https://github.com/HenkT28/pands-project/blob/master/Images/summary.png)

6. Iris_Histogram.py:

This provides 4 histograms of iris dataset features using matplotlib & sklearn.

The scikit-learn library comes with a few small standard datasets that do not require to download any file from some external website.

![Histogram](https://github.com/HenkT28/pands-project/blob/master/Images/Histogram.png)

7. Petal_Sepal_dist.py:

Reading Iris Dataset in Pandas Dataframe, then using matplotlib.pyplot library to create Scatter Plot, for all 3 species showing the petal and sepal distibution.

![petal_sepal_dist](https://github.com/HenkT28/pands-project/blob/master/Images/petal_sepal_dist.png)

8. Scatter_Plot.py:

Importing several packages, pandas, matplotlib.pyplot and seaborn, loading data set, and configuring scatter plot for Sepal Length and Sepal Width.

![scatter](https://github.com/HenkT28/pands-project/blob/master/Images/scatter.png)

9. Pairwise_Plot.py:

Imported libaries, and used Seaborn for creating Pairs Plot. The pairs plot makes high-level scatter plots to capture relationships between multiple variables within a dataframe. Used Seaborn, the statistical visualization library built on matplotlib.

![pairwise](https://github.com/HenkT28/pands-project/blob/master/Images/pairwise.png)

10. 3D_Scatter_Plot.py:

Imported libraries such as mpl_toolkits.mplot3d, and matplotlib.pyplot to see how a 3D graph shows the info.

It provides info on "sepal_length", in combination with "petal_length", and "petal_width".

![3D](https://github.com/HenkT28/pands-project/blob/master/Images/3D.png)

11. Iris_Boxplot.py:

Imported several libraries including seaborn, and used function boxplot, and stripplot, to display the differences between the 3 species of Iris for each of the 4 features. This produces great graphics, as you can see from below examples.

A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable.

A strip plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.

![boxplot_petal_length](https://github.com/HenkT28/pands-project/blob/master/Images/boxplot_petal_length.png)

![boxplot_petal_width](https://github.com/HenkT28/pands-project/blob/master/Images/boxplot_petal_width.png)

![boxplot_sepal_length](https://github.com/HenkT28/pands-project/blob/master/Images/boxplot_sepal_length.png)

![boxplot_sepal_width](https://github.com/HenkT28/pands-project/blob/master/Images/boxplot_sepal_width.png)


## Summary of Investigations and Conclusions

The start of each of the Python scripts lists the libraries used to generate some meaningful output, and graphics.

The first step to any data science project is to import your data. I used the read_csv() function from pandas to import this data. Also used genfromtxt function numpy package. And at other times, loaded Iris Data Set using Seaborn.

Loading CSV files specifically with pandas has become standard practice for working data scientists today.

As so many people have done extensive research into the Iris Data set, which explains the huge amount of resources available on the internet, I used a number of different approaches, and on top various libraries to get some meaningful output, and hopefully get a clear understanding why this Iris Data Set is so widely used throughout statistical science, especially for illustrating various problems in statistical graphics, multivariate statistics and machine learning.[8]

It's important to calculate the max, min and mean of each column, but just based on the output of these scripts, it's hard to draw any conclusions. The main point is to understand what the major differences are between these species of Iris especially where it concerns measurements of their petals and sepals (petal lengths and widths, sepal lengths and widths). And to show such differences visually is key.

So not only did I use histograms, also scatter plots. For a defintion of scatter plot, please go here:

https://en.wikipedia.org/wiki/Scatter_plot [18]

A scatter plot (also called a scatterplot, scatter graph, scatter chart, scattergram, or scatter diagram) is a type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data. A scatter plot can suggest various kinds of correlations between variables with a certain confidence interval. Correlations may be positive (rising), negative (falling), or null (uncorrelated). If the pattern of dots slopes from lower left to upper right, it indicates a positive correlation between the variables being studied. If the pattern of dots slopes from upper left to lower right, it indicates a negative correlation. A line of best fit (alternatively called 'trendline') can be drawn in order to study the relationship between the variables.


## [Analysis and Conclusions]

[1] Based on Iris_Data_Set_Describe script:

The count has the 4 features and 150 rows in total. From the results from Mean function it is clear, that sepal is larger than petal.

Running print(data.describe()) produces below summary:

![summary](https://github.com/HenkT28/pands-project/blob/master/Images/summary.png)

So this gives you some understanding on the Mean, Max and Min of the entire Iris data set.

The sepal length attribute has values that go from 4.3 to 7.9 and sepal width contains values from 2 to 4.4, while petal length values range from 1 to 6.9 and petal width ranges from 0.1 to 2.5. 

[2] Iris.Histogram & Petal_Sepal_Dist scripts:

From both graphics, you can draw very much the same conclusions - and while one is a histogram, the other is a scatter plot - they immediately provide you with some major observations:
* The feature "Petal width" can distinguish the targets better that other features. 

* Also to some great degree, the Petal length is unique for each of the 3 species. We can conclude that there is a difference among mean petal lengths for the different species of iris flowers. Thus, Petal Length is a good way to tell the flowers apart. 

* Virginia has the longest Sepal length, Petal length and Petal width.

* Setosa however has the longest Sepal width. 

* Also Setosa has the smallest Petal width and length, compared to both Versicolor and Virginica.

[3] Scatter_Plot script using Seaborn.

From this scattered plot, we can distinctly distinguish Setosa, but Iris Versicolor and Virginica can't be separated based on their sepal width and sepal length. Thus to distinguish between versicolor and virginica, we have to analyse some other features. 

There is considerable overlap between Iris Virginica and Iris Versicolor suggsting a high correlation and predictable relationship. 

To differentiate, here, we can use pairwise plotting.

[4] Pairwise_Plot script:

From the pairwise plots, we see that Setosa is distinguishable in all aspects. As for differentiating between Versicolor and Virginica, they can be seperated on the basis of Petal Length and Petal Width. In the plot between petal width verses petal length, the petal width and length of Versicolor is smaller than that of Virginica.

[5] 3D_Scatter_Plot script:

This script will give you a glance of the Iris data set showing in 3D format. As you can see, there is high concentration of samples where Sepal length is low, and Petal length is low as well. 

[6] Iris_Boxplot.py script:

The library seaborn, and functions boxplot, and stripplot, produce some great graphics as you can see. Again another way of displaying the differences between the 3 species of Iris for each of the 4 features. 

The box shows the high concentration, the high distribution of samples for this Iris Data Set. The other function, strip plot, gives another layer. It shows all observations, all samples taken for this Iris Data Set, along with some representation of the underlying distribution.

The graphics are really self explanatory, and complement my earlier findings.

![boxplot_petal_length](https://github.com/HenkT28/pands-project/blob/master/Images/boxplot_petal_length.png)

![boxplot_petal_width](https://github.com/HenkT28/pands-project/blob/master/Images/boxplot_petal_width.png)

![boxplot_sepal_length](https://github.com/HenkT28/pands-project/blob/master/Images/boxplot_sepal_length.png)

![boxplot_sepal_width](https://github.com/HenkT28/pands-project/blob/master/Images/boxplot_sepal_width.png)


### Prerequisites - how to run the code

1. Make sure you have Python installed, or Anaconda: 

[a] https://www.python.org/downloads/

Python is developed under an OSI-approved open source license, making it freely usable and distributable, even for commercial use. 

[b] Anaconda:

https://www.anaconda.com/distribution/

https://docs.anaconda.com/anaconda/

Anaconda® is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 1,500+ open source packages. Anaconda is free and easy to install, and it offers free community support.
Anaconda3 includes Python 3.7.

2. Also install Cmder software for running the python scripts from command line:

https://cmder.net/


### Running the python scripts.

Python can be run in two different ways: 

[a] interactive mode

[b] script mode

See below links for more info:

https://docs.python.org/3/tutorial/interpreter.html

https://en.wikibooks.org/wiki/Python_Programming/Interactive_mode

http://www.pybloggers.com/2017/10/coding-in-interactive-mode-vs-script-mode/

The normal mode, the script mode, is the mode where the scripted and finished .py files are run in the Python interpreter. Instead of having to run one line or block of code at a time (interactive mode), you can run all the code at once. 

As this problem set contains completed .py scripts, I suggest you run the scripts in normal mode. 

For example, from cmder go to the directory containing the .py scripts, by using cd command, and run the programs as follows:

python <script_name>.py


## Break down into end to end tests

I recommend you run the python scripts from command line, from cmder for example, but make sure you go to the right directory first containing the .py scripts, by using cd command, and then run the script as follows:

python <script_name>.py

There is no need to type in full script name, just by using the tab key on your keyboard it will auto-complete the script name automatically, from the folder location.


## Deployment

First of all I recommend you to go to the official Python website:

https://www.python.org/downloads/release/python-372/

As of now, 19/03/19. Python 3.7.2 is the latest version available for download and can be deployed on Windows, Linux/Unix, MacOS, and other operating systems.

I would suggest you consult the documentation carefully, and follow below links:

https://www.python.org/downloads/

https://docs.python.org/3.7/whatsnew/changelog.html#python-3-7-2-final


Alternatvely install the full Anaconda package which has Python functionality included.

## Built With

* [Python](https://www.python.org/downloads/) - The official Python website
* [cmder](https://cmder.net/) - Official cmder website
* [Anaconda](https://www.anaconda.com/distribution/) - The open-source Anaconda Distribution is the easiest way to perform Python/R data science and machine learning on Linux, Windows, and Mac OS X.

## Reading script code

If you want to read the script code, and accompanying Problem Assessment README, most text editors would be sufficient, but I recommend notepad ++ or even better visual studio code. 

https://code.visualstudio.com/

https://code.visualstudio.com/download

It's a free and open source. It has Integrated Git, debugging and extensions. 

It can be accessed from Cmder prompt, by typing the following shortcut:

λ code .

https://code.visualstudio.com/docs/setup/windows

Tip: 

Setup will add Visual Studio Code to your %PATH%, so from the console you can type 'code .' to open VS Code on that folder. 

[a] Make sure you go to the directory first containing the python scripts.

[b] Once you're in the correct directory, enter the shortcut command, and keep in mind there is a space between word code and the dot.

## References

[1] R. A. Fisher (1936). "The use of multiple measurements in taxonomic problems". Annals of Eugenics. 7 (2): 179–188. doi:10.1111/j.1469-1809.1936.tb02137.x.

[2] Edgar Anderson (1936). "The species problem in Iris". Annals of the Missouri Botanical Garden. 23 (3): 457–509. doi:10.2307/2394164. JSTOR 2394164.

[3] Edgar Anderson (1935). "The irises of the Gaspé Peninsula". Bulletin of the American Iris Society. 59: 2–5.

[4] "UCI Machine Learning Repository: Iris Data Set". archive.ics.uci.edu. Retrieved 2017-12-01.

[5] Software Freedom Conservancy. Git.

https://git-scm.com/

[6] Inc. GitHub. Github.

https://github.com/.

[7] GMIT. Quality assurance framework.

https://www.gmit.ie/general/quality-assurance-framework.

[8] Nick Cox - https://stats.stackexchange.com/a/74901

[9] Data SalaryMan - https://medium.com/@livingwithdata/exploring-the-iris-dataset-260cc1e5cdf7

[10] https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

[11] https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset

[12] https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

[13] https://www.datacamp.com/community/tutorials/pandas-read-csv

[14] https://stackoverflow.com/a/45721331

[15] https://mclguide.readthedocs.io/en/latest/sklearn/moreex1.html

[16] https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn

[17] https://github.com/kaggle/docker-python

[18] https://en.wikipedia.org/wiki/Scatter_plot

[19] https://en.wikipedia.org/wiki/Iris_flower_data_set

[20] https://etav.github.io/python/pairs_plot_python_seaborn.html

[21] https://guides.github.com/features/mastering-markdown

[22] https://matplotlib.org/users/pyplot_tutorial.html

[23] https://www.cs.odu.edu/~ccartled/Teaching/2017-Fall/DataAnalysis/Presentations/030-iris-dataset.pdf

[24] https://www.kaggle.com/lnbalon/iris-dataset-eda-and-classification-analysis

[25] https://seaborn.pydata.org/generated/seaborn.stripplot.html

[26] https://seaborn.pydata.org/generated/seaborn.boxplot.html

[27] https://www.datacamp.com/community/tutorials/introduction-machine-learning-python

