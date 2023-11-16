#Functions are a set of instructions which performs a specific task and can be reused multiple times
'''
Syntax:
def functionName (parameters):
    statements
    return something
 '''
 #def is used to declare a function
 #functionName is the name of the function
 #parameters consists of variables used by the function 
 #statements are the operations which we need to perform
 #return statement marks end of the function and return the output. Can be avoid if no value needed to be returned
'''
def helloWorld():
     print("Hello World")
helloWorld()
'''
###################################################
'''
def addNumbers(num1,num2):
    sum = num1 + num2
    print (sum)
    return
addNumbers(3,6)
addNumbers(400,500)
'''
###################################################
#To call a function
'''
Syntax:
functionName(parameters)
'''
###################################################
#Lambdas, also known as anonymous functions are small restricted functions which do not need a name
'''
syntax:
lambda p1,p2: expression
'''
#p1 & p2 are the parameters
adder = lambda x,y:x/y*100
print (adder(232,250))