
print("Program to swap two numbers and check whether first number is positive or negative \n")

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))


print("Before swapping the numbers first =", first, " and second = ", second)

if (first==0):
    print("The first number is Zero")
elif (first<0):
    print("The first number is Negative")
else:
    print("The first number is positive")

first, second = second, first
print("After swapping the numbers first =", first, "and second = ", second)


print("print all the numbers divisible by 4")

n = int(input("enter any number: "))

for i in range(n):
    if((i%4==0)):
        print(i)

print("Find the factorial of an input number\n")

n = int(input("Enter any number: "))
fact = 1
i = 1

while (i<=n):
    fact = fact * i
    i = i+1

print(f"The factorial of {n} is {fact}")



print("Menu driver program to build simple calculator functions\n")

n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
operator = input("Enter any Operator (+, -, /, *) : ")

result = 0.0
if operator in ('+', '-', '/', '*'):
    if(operator == '+'):
        result = n1+n2
        print(f"The Sum Of The Input Number {n1} and {n2} is {result}")
    
    elif(operator == '-'):
        result = n1-n2
        print(f"The Difference Of The Input Number {n1} and {n2} is {result}")
        
    elif(operator == '*'):
        result = n1*n2
        print(f"The Multiplication Of The Input Number {n1} and {n2} is {result}")
    else:
        result = n1/n2
        print(f"The Division Of The Input Number {n1} and {n2} is {result}")
else:
    print("Please Enter Valid Operator !!")

print("Fibonacci series of 'n' number \n")

terms = int(input("Enter no.of terms : "))

n1, n2 = 0, 1
count = 0

if terms <= 0:
   print("Please enter a positive integer")

elif terms == 1:
   print(f"Fibonacci sequence up to {terms} : ")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < terms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1