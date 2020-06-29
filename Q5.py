# Write a Python program to read a file line by line store it into a variable

def read(a):
        with open (a) as file:
                cse=file.readlines()
                print(cse)
a=input("enter the file name:")
read(a)