'''A dictionary is a data structure which contains data in the form of keys and values.
A key and value pair forms an item in the dictionary. A key is usually a string
items are seperated by commas, keys and values are seperated by colon (:).
items in the dictionary are enclosed within curly brackets

dict1= {\n\t'name':'xyxz',\n\t'age':25,\n\t'hobby':'Dancing' \n}

'''
dict1= {'name':'xyxz','age':25,'hobby':'Dancing' }
dict1['hobby']
print(dict1['hobby'])
print(dict1)

# In dictionary we can either add a new key-value pair or update an existing one
dict2= {'name':'xyxz','age':25,'hobby':'Dancing' }
dict2['name'] = 'Mrudhul'
dict2['Profession'] = 'IT Engineer'
print(dict2)

#Deleting data
#In dictionary we can either remove an individual item or the entire dictinary

dict3= {'name': 'Mrudhul', 'age': 25, 'hobby': 'Dancing', 'Profession': 'IT Engineer'}
del dict3['age']
print(dict3)

#to delete entirely
del dict1
#to remove all the items in the dictionary
dict3.clear(              )
print(dict3)