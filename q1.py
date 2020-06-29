# Write a Python program to read an entire text file

def read(a):
        txt = open(a)
        print(txt.read())
a=input("enter the file name:")
read(a)