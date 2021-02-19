###Python Libraries
# Python, like other programming languages, has an abundance of additional modules or libraries that augument the base framework and functionality of the language.

# Think of a library as a collection of functions that can be accessed to complete certain programming tasks without having to write your own algorithm.
# For this course, we will focus primarily on the following libraries:

# Numpy is a library for working with arrays of data.

# Pandas provides high-performance, easy-to-use data structures and data analysis tools.

# Scipy is a library of techniques for numerical and scientific computing.

# Matplotlib is a library for making graphs.

# Seaborn is a higher-level interface to Matplotlib that can be used to simplify many graphing tasks.

# Statsmodels is a library that implements many statistical techniques.

##Documentation
#Reliable and accesible documentation is an absolute necessity when it comes to knowledge transfer of programming languages. Luckily, python provides a significant amount of detailed documentation that explains the ins and outs of the language syntax, libraries, and more.
#Understanding how to read documentation is crucial for any programmer as it will serve as a fantastic resource when learning the intricacies of python.
#Here is the link to the documentation of the python standard library: Python Standard Library

##Importing Libraries
#When using Python, you must always begin your scripts by importing the libraries that you will be using.

#The following statement imports the numpy and pandas library, and gives them abbreviated names:

import numpy as np
import pandas as pd

# Utilizing Library Functions
# After importing a library, its functions can then be called from your code by prepending the library name to the function name.
# For example, to use the 'dot' function from the 'numpy' library, you would enter 'numpy.dot'.
# To avoid repeatedly having to type the libary name in your scripts, it is conventional to define a two or three letter abbreviation for each library, e.g. 'numpy' is usually abbreviated as 'np'.
# This allows us to use 'np.dot' instead of 'numpy.dot'. Similarly, the Pandas library is typically abbreviated as 'pd'.

# The next cell shows how to call functions within an imported library:
print("\nArray with Numpy")
a = np.array([0,1,2,3,4,5,6,7,8,9,10])
print(np.mean(a))
#As you can see, we used the mean() function within the numpy library to calculate the mean of the numpy 1-dimensional array.

## Data Management
# Data management is a crucial component to statistical analysis and data science work. The following code will show how to import data via the pandas library, view your data, and transform your data.
# The main data structure that Pandas works with is called a Data Frame. This is a two-dimensional table of data in which the rows typically represent cases (e.g. Cartwheel Contest Participants), and the columns represent variables. Pandas also has a one-dimensional data structure called a Series that we will encounter when accesing a single column of a Data Frame.
# Pandas has a variety of functions named 'read_xxx' for reading data in different formats. Right now we will focus on reading 'csv' files, which stands for comma-separated values. However the other file formats include excel, json, and sql just to name a few.
# This is a link to the .csv that we will be exploring in this tutorial: Cartwheel Data (Link goes to the dataset section of the Resources for this course)
# There are many other options to 'read_csv' that are very useful. For example, you would use the option sep='\t' instead of the default sep=',' if the fields of your data file are delimited by tabs instead of commas. See here for the full documentation for 'read_csv'.

## Importing Data
# Store the url string that hosts our .csv file (note that this is a different url than in the video)
url = "Cartwheeldata.csv"

# Read the .csv file and store it as a pandas Data Frame
df = pd.read_csv(url)

# Output object type
print(type(df))

## Viewing Data

# We can view our Data Frame by calling the head() function
print(df.head())
# The head() function simply shows the first 5 rows of our Data Frame. If we wanted to show the entire Data Frame we would simply write the following:
# Output entire Data Frame
print(df)

#As you can see, we have a 2-Dimensional object where each row is an independent observation of our cartwheel data.
#To gather more information regarding the data, we can view the column names and data types of each column with the following functions:

print(df.columns)

## Lets say we would like to splice our data frame and select only specific portions of our data. There are three different ways of doing so.
# 1-.loc()
# 2-.iloc()
# 3-.ix()
# We will cover the .loc() and .iloc() splicing functions.

## loc()
# .loc() takes two single/list/range operator separated by ','. The first one indicates the row and the second one indicates columns.

# Return all observations of CWDistance
print(df.loc[:,"CWDistance"])

# Select all rows for multiple columns, ["CWDistance", "Height", "Wingspan"]
print(df.loc[:,["CWDistance", "Height", "Wingspan"]])

# Select few rows for multiple columns, ["CWDistance", "Height", "Wingspan"]
print(df.loc[:9, ["CWDistance", "Height", "Wingspan"]])

# Select range of rows for all columns
print(df.loc[10:15])

# The .loc() function requires to arguments, the indices of the rows and the column names you wish to observe.
# In the above case :** specifies all rows, and our column is **CWDistance. df.loc[:**,"CWDistance"**]
# Now, let's say we only want to return the first 10 observations:
print(df.loc[:9, "CWDistance"])

##.iloc()
# .iloc() is integer based slicing, whereas .loc() used labels/column names. Here are some examples:
print(df.iloc[:4])
print(df.iloc[1:5, 2:4])

# Typeerror
# print(df.iloc[1:5, ["Gender", "GenderGroup"]])
# We can view the data types of our data frame columns with by calling .dtypes on our data frame:

print(df.dtypes)
#The output indicates we have integers, floats, and objects with our Data Frame.

#We may also want to observe the different unique values within a specific column, lets do this for Gender:
# List unique values in the df['Gender'] column
print(df.Gender.unique())
# Lets explore df["GenderGroup] as well
print(df.GenderGroup.unique())

#it seems that these fields may serve the same purpose, which is to specify male vs. female. Lets check this quickly by observing only these two columns:
# Use .loc() to specify a list of mulitple column names
print(df.loc[:,["Gender", "GenderGroup"]])

# From eyeballing the output, it seems to check out. We can streamline this by utilizing the groupby() and size() functions.
print(df.groupby(['Gender','GenderGroup']).size())

# This output indicates that we have two types of combinations.

# Case 1: Gender = F & Gender Group = 1
# Case 2: Gender = M & GenderGroup = 2.
# This validates our initial assumption that these two fields essentially portray the same information.