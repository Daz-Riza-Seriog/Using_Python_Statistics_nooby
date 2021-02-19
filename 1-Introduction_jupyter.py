### What is Jupyter Notebooks?
# Jupyter is a web-based interactive development environment that supports multiple programming languages, however most commonly used with the Python programming language.
# The interactive environment that Jupyter provides enables students, scientists, and researchers to create reproducible analysis and formulate a story within a single document.
# Lets take a look at an example of a completed Jupyter Notebook: Example Notebook

##Jupyter Notebook Features
# File Browser
# Markdown Cells & Syntax
# Kernels, Variables, & Environment
# Command vs. Edit Mode & Shortcuts

##What is Markdown?
#Markdown is a markup language that uses plain text formatting syntax. This means that we can modify the formatting our text with the use of various symbols on our keyboard as indicators.

#Some examples include:

#Headers
#Text modifications such as italics and bold
#Ordered and Unordered lists
#Links
#Tables
#Images
#Etc.
#Now I'll showcase some examples of how this formatting is done:


print("This is a python code cell")

#A kernel is the back-end of our notebook which not only executes our python code, but stores our initialized variables.

### For example, lets initialize variable x

x = 1738

print("x has been set to " + str(x))

### Print x

print(x)

#Issues arrise when we restart our kernel and attempt to run code with variables that have not been reinitialized.
#If the kernel is reset, make sure to rerun code where variables are intialized.

## We can also run code that accepts input

name = input("What is your name? ")

print("The name you entered is " + name)

#It is important to note that Jupyter Notebooks have in-line cell execution.
#This means that a prior executing cell must complete its operations prior to another cell being executed. (same in Pycharm)
#A cell still being executing is indicated by the [*] on the left-hand side of the cell.

print("This won't print until all prior cells have finished executing.")
