
#############* Advanced Topics of Python #############

#* Exception == Events detected during execution that interrupt the flow of a program

try:
    num = int(input("Enter any numerator: "))
    den = int(input("Enter any denominator: "))
    result = num/den

except ZeroDivisionError as e:                  # as e : will print the actual error in terminal
    print("You can't divide by 0")
    print(e)

except ValueError as e:
    print("Enter number only plz! ")
    print(e)

except:
    print("Something went wrong :(")

else:                                           # Writing results in an else block is always a good practice.
    print(f"Answer: {result}")

finally:
    print("\n")
    print("Code written under finally block will print whether try block code runs or not")
    

import os                                       #! Necessary if we want to perform file handling operations
# print(dir(os))                                # To print all the functions present under os library

path1 = "/home/bunny/Desktop/SaxX/Snapcodes/tp.txt"
path2 = "/home/bunny/Desktop/SaxX/Snapcodes/folder"

if os.path.exists(path2 and path1):
    print("Location Exists!")
    if os.path.isfile(path1):
        print("That is a file!")
    if os.path.isdir(path2):
        print("That is a directory!")
else:
    print("Location Doesn't Exists!")


#* Reading a File 

try:                                            # Do note, writing file handling commands in try block is always helpful while dealing with errors.
    with open('test.txt') as file:              # By default it's on read mode.. 
        print(file.read())
    print(file.closed)                          # we don't need to forcefully close files manually in python.
except:
    print("That file was not found :(")

#* Writing in a File 

try:
    text = "Heyooooo\nThis is written via 'write' operation\n"    
    with open('test.txt','w') as file:              # Write operation always overwrite the previous texts, better to use 'append'
        file.write(text)

#* Appending in a File

    text2 = "And this is written via 'append' operation"
    with open('test.txt','a') as file:
        file.write(text2)
except:
    print("Something went wrong :(")

import shutil                                   #! All copy funcs are present in a this library
# print(dir(shutil))

shutil.copyfile('test.txt','test2.txt')         # src,dest
# copyfile() = copies only content of a file
# copy() = copyfile() + permission mode + dest can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

