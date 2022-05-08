#for deleting the file
import os as myOS
myOS.remove("Bhanu.txt")
if myOS.path.exists("demofile.txt"):
    myOS.remove("demofile.txt")
else:
    print("The file does not exist")