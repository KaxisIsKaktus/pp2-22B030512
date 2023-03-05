import os 
EngAlphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
ListOfAlphabet = list(map(str , EngAlphabet.split(" "))) 
for char in ListOfAlphabet:    
    with open( "C:/pp2/pp2-22B030512/TSIS6/dir-and-files/smth/" + char +".txt", "w") as file:
        file.write("KAXIS IS KAKTUS")