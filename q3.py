# Write a Python program to append text to a file and display the text

def read(a):
        from itertools import islice
        with open(a,"w") as file:
                file.write("Python Exercises\n")
                file.write("Java Exercises")
        txt = open(a)
        print(txt.read())
read('salma.txt')