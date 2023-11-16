'''List is a data structure in python which is used to hold multiple values, 
just like what you do with a shopping list
. Data Structure is a format for storing data'''
,# A list contain,s items seperated by commas, These items are enclosed with in square brackets
#eg: list1=[2,4,5,3,7,6,9]
#eg: list2 = [4, "Hi", 15, "Demo"]
'''The items in the list are identified using their positions
These positions are known as indexes, indexes starts from 0'''
list1 = [2,4,5,3,7,6,9]
list1[3]
print(list1[1])
a = list1[1:4]
print(a)
#update the data into the list
list2 = [4,55,33,66,77,89]
list2[4]=100
list2.append(150)
print(list2)
#delete data from the list
list2 = [4,55,33,66,77,89]
del list2[2]
# (aka)=>  list2.remove(33)
print(list2)
