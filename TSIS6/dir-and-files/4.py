import os
with open(r"C:\pp2\pp2-22B030512\TSIS6\dir-and-files\polish-cow.txt" ,'r') as file:
    data = file.readlines()
print(f"There is {len(data)} lines")