'''Tuple is a data structure just like list to hold multiple values
A tuple is a sequence of items seperated by commas
These items are enclosed within parantheses (round brackets)
eg: tuple = (2,4,5,6,7,8,2)
    tuple1= (4, "Hi", 56, "Me")
'''
tuple = (2,4,5,6,7,8,2)
tuple[1]
print(tuple[1])
print(tuple[1:4])
print(tuple)
print(tuple[:5])

#update & Delete data
#unlike list, tuples are immutable(items in a tuple cannot be updated nor deleted)
#but we can delete tuple entirely (cannot delete one element)
del tuple
