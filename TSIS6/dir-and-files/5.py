import os 
list = ["There" , "was" , "Polish" , "Cow", "lyrics"]
with open(r"C:\pp2\pp2-22B030512\TSIS6\dir-and-files\polish-cow.txt" , "w+") as myFile:
    for word in list:
        myFile.write(word + "\n")