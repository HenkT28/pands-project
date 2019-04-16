# Project 2019 - Programming and Scripting

This readme contains background info, instructions, and research into the well-known Fisher’s Iris data set, for Programming and Scripting module (GMIT H.Dip Data Analytics - Academic Year 2019 - 2020).

Student: Henk Tjalsma

GMIT email address: G00376321@gmit.ie

## Problem statement
The project entails researching the data set, and then writing documentation and code in the Python programming language based on that research.

1. Go to Github web site - User Account: HenkT28 

(https://github.com/HenkT28)

2. Click on the download button, and copy/paste the link:

https://github.com/HenkT28/pands-project.git

## Fisher’s Iris data set

https://en.wikipedia.org/wiki/Iris_flower_data_set


The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper:

* The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[1] 


It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.[2] 

Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".[3]


The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). 
Photo's Iris flowers of the three related species:

1. Images\Iris_setosa.jpg

2. Images\Iris_versicolor.jpg

3. Images\Iris_virginica.jpg


Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. 
Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. 

Images\Iris_dataset_scatterplot.svg.png

Images\Spectramap_Biplot_Iris_Flower_Data_Set_FULL.jpg


Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.[4]


## Data Set

The dataset contains a set of 150 records under five attributes - petal length, petal width, sepal length, sepal width and species.

The iris data set is widely used as a beginner's dataset for machine leaning purpose. 

Here are some lines of python code that definess how this works:

Images\Some lines how Python works.png

### Python Packages used for analyzing this Iris Data Set

[1]. Pandas/Numpy (also for reading in csv file):

https://pandas.pydata.org/

[2]. Matplotlib & Pyplot

https://matplotlib.org/

https://matplotlib.org/api/pyplot_api.html

[3]. Seaborn

https://seaborn.pydata.org/

For example:
https://seaborn.pydata.org/examples/scatterplot_matrix.html

import seaborn as sns

sns.set(style="ticks")

df = sns.load_dataset("iris")

sns.pairplot(df, hue="species")

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


## Below what each script does


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



