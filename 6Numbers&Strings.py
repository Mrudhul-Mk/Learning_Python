'''
pow()  - it takes two number and returns the result of the first number raised to the power of the second
To use all these function we need to import a math module
A module is an external python file that contains functions that are used by other python programs

syntax:
import MODULENAME

to access any function we write as 
MODULENAME.FUNCTIONNAME()
'''
import math
y = math.pow(4,3)
print("pow value:", y)

# math.floor() - takes in a number as a parameter and returns the largest integer equal or less than the number passed as the parameter
import math
a = math.floor(4.3)
b = math.floor(10.9)
a1 = math.ceil(4.3)
b1 = math.ceil(10.9)
print(a)
print(b)
print(a1)
print(b1)
#fabs() - function takes in one parameter and returns its absolute value (absolute value is a number irrespective of its signs +ve or -ve)
c = math.fabs(10)
d = math.fabs(-10)

print("fabs ",c)
print ("fabs ",d)

'''
math.log() can take either one or two parameters.
when one parameter is passed it returns the natural logarithm of that number
when two parameter are passed it returns the logarithm of the first number to the base of the second number'''
e = math.log(10)
f = math.log(10,2)
print (e)
print(f)

#math.sqrt() - function is used to find the square root

g = math.sqrt(9)
print (g)
#apart from these math module consists of numerous other functions such as trignometric and hyperbolic functions
#----------------------------------------------------------------------------------------------------------
#Strings
'''
Textual data in programming languages is represented by using strings
A string is a sequence of character spaces and numbers'''
str = "here i Am"
str.capitalize()
str.count('e')
str.find("h")

#Concatenation
str = ""
line = (" Sorry " , "for the delay")
str.join(line)