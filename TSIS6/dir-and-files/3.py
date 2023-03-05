import os 
somePath = r"C:\pp2\pp2-22B030512\TSIS6\dir-and-files\polish-cow.txt"
if os.path.exists(somePath):
    print("Path to something exist , let's find the filename and dirname" )
    print( "Name of the file: " + os.path.basename(somePath))
    print( "Name of the directory: " + os.path.dirname(somePath))
else:
    print("Path doesn't exist") 