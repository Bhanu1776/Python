#for writing into the file
myFile = open("Bhanu.txt", "a")
myFile.write("\nAdding More Content To The File")
myFile = open("Bhanu.txt", 'r')
for x in myFile:
    print(x)
myFile.close()