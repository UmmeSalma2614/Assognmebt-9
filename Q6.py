# Write a Python program to read a file line by line and store it into a list

def read(a):
        with open(a) as file:     
                list = file.readlines()
                print(list)
a=input("enter the file name:")
read(a)