import math

###Data Types in Python
#The following data types can be used in base python:

#*boolean*
#*integer*
#*float*
#*string*
#*list*
#*None*
#complex
#object
#set
#dictionary
#*We will only focus on the bolded ones*

#Let's connect these data types to the the variable types we learned from the Variable Types video.

#Numerical or Quantitative (taking the mean makes sense)
#Discrete
# Integer (int) #Stored exactly
#Continuous
# Float (float) #Stored similarly to scientific notation. Allows for decimal places but loses precision.

print(type(4))
print(type(0))
print(type(-3))
#try taking the mean
print('\nTry taking the mean')
numbers = [2, 3, 4, 5]
print(sum(numbers)/len(numbers))
print(type(sum(numbers)/len(numbers))) #In Python 3 returns float, but in Python 2 would return int
print(3/5)
print(6*10**(-1))
print(type(3/5))
print(type(math.pi))
print(type(4.0))

# Try taking the mean
print('\nTry taking the mean')
numbers = [math.pi, 3/5, 4.1]
print(type(sum(numbers)/len(numbers)))
# Boolean
print('\nBoolean')
print(type(True))
# Boolean
if 6 < 5:
    print("Yes!")

myList = [True, 6<5, 1==3, None is None]
for element in myList:
    print(type(element))

print(sum(myList)/len(myList))
print(type(sum(myList)/len(myList)))

#String
print('\nString')
print(type("This sentence makes sense"))
print(type("Makes sentense this sense"))
print(type("math.pi"))

#This is a TypeError
#strList = ['dog', 'koala', 'goose']
#print(sum(strList)/len(strList))

#Nonetype
print('\nNoneType')
# None
print(type(None))
# None
x = None
print(type(x))
#This is a TypeError
#noneList = [None]*5
#print(sum(nonList)/len(nonList))

#Lists
#A list can hold many types and can also be used to store ordinal information.
print('\nList')
# List
myList = [1, 1.1, "This is a sentence", None]
for element in myList:
    print(type(element))

#This is a TypeError
#print(sum(myList)/len(myList))

# List
myList = [1, 2, 3]
for element in myList:
    print(type(element))
print(sum(myList)/len(myList)) # note that this outputs a float

myList = ['third', 'first', 'medium', 'small', 'large']
print(myList[0])

myList.sort()
print(myList)