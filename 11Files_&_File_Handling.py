#A file can be stored in different folders in a drive. Each folder is seperated by a backslash(\).
'''The in-built methods in python can handled two major types of files - Text files and Binary files

The test and binary files have .tct and .bin as their extension respectively

Test files are used to store human readable information whereas the binary files contain 
computer readable information that are written using bunary(0s and 1s)

As Files are non-volatile in nature, the data will be stored permanently and using python 
we will handle these files in our application

File Processing takes place in the following order
1. Open a file that returns a filehandle(File Object)
2. Use the handle to perform read or write action
3. Close the file
'''

#different file handling operations.

#1. Opening a file in python
'''To open a file in python we use its built-in open() function
This function returns a file object, that would be utilized to call other methods associated with it
you can use it to read or modify the file

Syntax: 
file object = open(file_name, access_mode)

file_name: it is the name of the file which needs to be opened
access_mode : it specifies the mode of the file needed to be open such as read, write and so on
              by default, it will be in the read-mode

we can specify the mode while opening a file, to specify whether we want to read(r), write(w) or append(a) to the file
'''

#6 access modes available in python to work with a text file
'''r - Read mode is used only to read data from the file. it is also the default mode
   w - It will create a new file if it doesn't exist, otherwise will overwrite the file and allow you to write to it
   a - it will write data to the end of the file. It does not erase the existing data and the file must exist for this mode
   r+ - it opens the file to read and write both. the file pointer will be at the beginning of the file
   w+ - The exact same as r+ but if the file doesn't exist, a new one is made else the file is overwritten
   a+ - similar to w+ as it will create a new file if the file doesn't exist.Otherwise file pointer will be at the end of the file if exist
   '''
   
'''To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:
By default the read() method returns the whole text, but you can also specify how many characters you want to return by read(N)
By calling readline() two times, you can read the two first lines:
'''
path = 'c:/Users/mrudh/OneDrive/Desktop/My Projects/Learning python/Learning_Python/days.txt'
myFile = open ('path','r')

#read() function:
# file_handle.read(N)
myFile.read()

#Alter
'''
path = 'c:/Users/mrudh/OneDrive/Desktop/My Projects/Learning python/Learning_Python/days.txt'
myFile = open('path')
print(myFile.read())
'''
'''
path = 'c:/Users/mrudh/OneDrive/Desktop/My Projects/Learning python/Learning_Python/days.txt'
myFile = open('path')
print(myFile.readlines())
'''
#python provides the write() method to write a string or sequence of bytes to a file
file_input = open("read.txt",'w')
file_input.write("This is my first Line \n Hello Developer \n Welcome to file handling")
print(file_input.read())

file_input = open("read.txt",'a')
file_input.write("\nPython is amazing second line \n Thanks.")
print(file_input.read())

#Closing a file
file_input = open("read.txt",'r')
print(file_input.read())
file_input.close()
