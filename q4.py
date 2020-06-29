# Write a Python program to read last n lines of a file

def LastNLines(f,n):
    with open(f) as file:
        print('Last',n,"lines from file:",f)
        for line in (file.readlines() [-n:]):
            print(line, end='')
name=input("enter the file name:" )
n= int(input("no of last lines to read:"))
try:
    LastNLines(name,n)
except:
    print("file error....")