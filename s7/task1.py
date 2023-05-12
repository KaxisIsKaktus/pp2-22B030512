import os
from os.path import exists

def existFile(fname):
    file_exist = exists(fname+".txt")
    if (file_exist == 1):
        file_name = input('Please enter a file name (WITHOUT EXTENTION, .txt will be added automatically):').strip()
    return file_exist
    


def createFile(fname):
    f = open(fname+".txt", "a")
    f.close()
    print("FIle " + fname+".txt successfully created")

def readFile(fname):
    f = open(fname+".txt", "r")
    print(f.read())
    f.close()

def appendFile(fname, lol):
    f = open(fname+".txt", "a")
    f.write(lol)
    f = open(fname+".txt", "r")
    print(f.read())

def overwriteFile(fname, lol):
    f = open(fname+".txt", "w")
    f.write(lol)
    f = open(fname+".txt", "r")
    print(f.read())

def removeFile(fname):
    print('\n')
    os.remove(fname+".txt")
    print("File " + fname+".txt successfully remored")


print('Welcome to my blog!\nWhat do you want to do with files/the file?')
option = int(input('Options(type a number):\n1-Create a new file\n2-Read existing file\n3-Update some information in a file\n4-Overwrite all content in a file\n5-Remove existing file\nWrite a number(1-5): '))

file_name = input('Please enter a file name (no extension, .txt will be added automatically):').strip()

if(existFile(file_name) == 0):
    if option == 1:
        createFile(file_name)
    elif option == 2:
        readFile(file_name)
    elif option == 3:
        print("\n*******************\n")
        lol = input()
        print("\n*******************\n")
        appendFile(file_name, lol)
    elif option == 4:
        print("\n*******************\n")
        lol = input()
        print("\n*******************\n")
        overwriteFile(file_name, lol)
    elif option == 5:
        removeFile(file_name)
    else:
        print('Something went wrong!')