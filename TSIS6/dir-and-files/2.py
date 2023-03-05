import os 
path = r"C:\pp2\pp2-22B030512\TSIS6\dir-and-files\polish-cow.txt"
data = open(path) 
if os.path.exists(path):
    print("File and path exists let's check readability!")
    if data.readable():
        print("Wonderful! we may read this file so let's chek the writability!")
        if os.access(path , os.W_OK):
            print("Perfect! we may write something in this file so let's check the executability!")
            if os.access(path , os.X_OK):
                print("OH MY GOD! this file is executable!")
                answer = input("Finally do you want to read this file ? (put Y|N) ") 
                if answer == "Y" or answer == "y":
                    print(data.read()) 
            else:
                print("This file isn't executable. (T_T)") 
        else:
            print("We can't write anything in this file! ")
    else:
        print("Unfortunately we can't read thie file!")
else:
    print("Its kinda sus! File doesn't exist!")