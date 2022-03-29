print("Hello World")                    # Python is case sensitive language ..
                                        # Python does not need a compiler because it relies on an application (called an interpreter)

#* Variables ..
name = "Bunny"
age = 19
print("My name is", name,"and my age is",age)
print(f"My name is {name} and my age is {age}") # Another way to print with the help of f-string

is_adult = True                                 # Boolean variables are also accepted in python


#* Taking inputs from user in python

name1 = input("Enter your name: ")
print("Hello " + name1)


#* Type Conversion 
                                                # Very IMP
old_age = input("Enter your old age: ")         # Inputs are always store in the form of string only ..
new_age = int(old_age) + 2                      # int() func is used to convert string input to integer 
print(new_age)

number = 18
print(float(number))

#* Print sum of Two numbers 

first = input("Enter first number: ")
second = input("Enter second number: ")
sum = int(first) + int(second)                  # Here type conversion is imp, else the output will be different
print("The sum is: " + str(sum))                # sum has to be in string format, otherwise string and int will never concatenate


#* Strings in python

name2 = "Bhanu Sunka"
print(name2.upper())                            # upper() is the method used for strings ..

print(name2.find('S'))                          # find() method will find any character in String
print(name2.find('z'))                          # Here 'z' is not present so output will be -1
print(name2.replace("Bhanu Sunka", "Bunny"))

print('n' in name2)                             #* 'in' is the keyword
print("Bunny" in name2)                         # 'in' keyword is used to find the sub-string or char present in that string .. will return output in boolean


#* Arithmetic operators in python

print(5+2)
print(5*2)

print(5/2)                                      # Answer will be in float 
print(5 // 2)                                   # Here answer will be in int only .. Also known as 'Floor division' operator 

print(5%2)
print(5 ** 2)                                   # '**' is known as power or Exponent operator .. i.e 5 square is 25


#* Shortcuts for arithmetic operations 

i = 5
i = i + 2                                       # This can be written as.. watch below line

i += 2                                          # Both means the same .. #* This one is shortcut
i -= 2
i *= 2
print(i)


#* Comparision operator in python

print(3 > 2)                                    # By default comparision operators are predefined by boolean data type .. so the output will either True or False
print(3 == 2)                                   # If both are equals then true or else false
print(3 != 3)                                   # Reverse output


#* Logical operators in python

print(2>3 or 2>1)                               # 'or' is the keyword.. #* If anyone one value is True then whole operation will be true

print(3>2 and 2>1)                              # 'and' is the keyword.. #* If both values are True then only True, else False

print(not 3>2)                                  # 'not' is the keyword.. #* This usually reverse the value True becomes False and vice-versa


#* Conditional operators

age = 22

if age >= 18:
    print("You are an adult")
elif age<18 and age>3:
    print("You are not an adult")
else:
    print("You are a baby :)")
print("Thank You!!")                            # This statement is not under else condition, So check indentation


#* Range in python

numbers = range(5)                              # Now range will not include 5 .. output will be 0,1,2,3,4
print(numbers)


#* Loops in python

i = 1
while i <= 5:
    print(i)
    i = i + 1

for i in range(5):
    print(i)


#* Lists in python

marks = [95, 89, 74.5, "marks"]                 # In lists we can store any kind of data types.. 
                                                #* We can identify lists by square brackets '[]'
print(marks)
print(marks[0])                                 # We can print any value present in lists by specifying index position
print(marks[-1])                                # In lists reverse indexing is also possible .. Here the output will be last value 
print(marks[0:3])                               # This way is used to print the start and the before end of the list by mentioning index positions..

print("\n")

for score in marks:                             #* With the help of for loops, we can print the lists in python
    print(score)

marks.append(99)                                # Append is used to add values at the end !!
marks.insert(0, 63)                             # With the help of insert method we can insert values at any index position
print(marks)
print(99 in marks)                              # By this way we can find any value present in list ..
print(len(marks))                               # This will print the length of that list

print("\n")

a = 0
while a < len(marks):                           #* By using while loops also we can print the lists in python
    print(marks[a])
    a = a + 1

marks.clear()                                   # This will clear all the values present in list
print(marks)

#* Break and continue 

students = ["Bhanu", "Yash", "Farhan", "Shaun", "Prajakta", "Gauri"]

for boys in students:
    if boys == "prajakta":
        break                                   # whenever break is included the loop will stop at that value 
    print(boys)

print("\n")

for student in students:
    if student == "Prajakta":
        continue                                # continue will skip the specified value in a loop
    print(student)


#* Tuples in Python
                                                # Tuples are immutable .. i.e once we declare then we can't change values
marks3 = (95, 98, 97, 97, 97)                   #* we can identify tuples with the help fo Round brackets '()'
# marks3[0] = 91                                we can't do this bcoz tuples are immutable that is we cannot add or remove values once we declared tuple
print(marks3)

persons = "Bhanu", "Bunny", "Babblu"            #* we can also initialise tuple without Round brackets 

# We can perform two operations in tuples
print(marks3.count(97))                         # This will print the number of 97's present in tuple
print(marks3.index(97))                         # This will print the index position of that specific value 


#* Sets in python
                                                # Only unique values(elements) can be stored in sets .. duplicates are not allowed
marks4 = {95,98,91}                             #* We can identify sets by Curly brackets '{}'
print(marks4)

for scores in marks4:                           # Another way to print sets
    print(scores)

# print(marks4[0])                              # In sets indexing doesn't exist
                                                #* Since sets doesn't have indexing, So sets are unordered by nature


#* Dictionary in python
                                                # Dictionaries are same as sets, but dictionary contains 'Elements'
                                                #* 'Elements' are further divided into two parts i.e 'key' and 'value'
marks5 = {"English":95, "Chemistry":99, "Maths":98}     # Here subjects are keys, and marks are values
print(marks5)

print(marks5["Chemistry"])                      # Now we can find values with the help of keys ..

marks5["Physics"] = 91                          # This is how we can add new 'Element' in a dictionary
print(marks5)

marks5["Physics"] = 92                          # In this way we can change any value with the help of key
print(marks5)


#* Functions in python

import math                                     #! Header file, If we want to use maths predefined functions in python
from math import *                              # Another way to import all functions present in math library
print(dir(math))                                #* This will print all the available functions present in math library

print("\n")

from math import sqrt                           #! We can also import required functions, rather than importing all functions
print(sqrt(16))

# User-defined Functions

def print_sum(first, second=4):                 # Function defination
    print(first + second)

print_sum(1)                                    # Function call


#* Lambda Function

x = lambda y : y * 2                            # 'lambda' is the keyword, y is the local variable that is created under a function
print(x(5))                                     

a = lambda p,q: p*q                             # multiply two numbers using lambda
print(a(3,10))


def mul(u):                                     # Lambda inside a function
    return lambda v: u * v
result = mul(5)  
print(result(4)) 


#* Types of Scopes

# 1) Local variable 
def aFun():
    var1 = "I m a local variable"
    print(var1)
aFun()
# print(var1)

# 2) Global Variable 
var2 = "I m a global variable"
def aFun():
    print(var2)
aFun()
print(var2)

# Functions inside a function
def parentFun():
    var3 = "I m a variable"
    print(var3)
    def childFun():                             # This func is present inside another func, In this case 2nd func can also use 1st func variables
        print(var3)
    childFun()
parentFun()


#* Global keyword
                                                # 'Global' keyword to create a variable that can be accessed globally..
def myFunc():
    global x3                                    # we can declare global variable inside a func by using 'Global' keyboard
    x3 = "A global variable"
    print(x3)
myFunc()
print(x3)


# Exception
x2 = "A global variable"                         
print(x2)
def myFunc():
    global x2                                    # If already a global variable is present then func global variable with same name will replace ..
    x2 = "I'm a variable"
    print(x2)
myFunc()
print(x2)


#* ______________________________________________________________________________________________________________________

#* This is how we can differentiate data structures..

#* [] --> Lists
#* () --> Tuples
#* {} --> Sets and Dictionaries 