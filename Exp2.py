l1 = [1,2,3,4,5,6,7,8,9]
summ = 0
print("Current array is:",l1)

for i in l1:
    if (i%2==0):
        summ = i + i
print("Sum of all even elements are:",summ)

count = 0
for j in l1:
    if (j%3==0):
        count = count + 1
print("The number of elements which are divisible by 3 are:",count)
print("\n")

l1.append(10)
l1.append(11)
print("Array after adding two elements at the end:",l1)
print("\n")

for i in l1:
    if (i%2==1):
        l1.remove(i)
print("Array after deleting all the odd elements :",l1)

l2 = []
l2 = input("Enter multiple words or a paragraph: ")

print("No.of character in a list are :",len(l2))

l2words = l2.split(" ") 
print("No.of words in a list are :",len(l2words))

newParaGraph = "Hello"
fWord = input("Enter the substring you want to replace in the string : ")
fRep = input("Enter the new replace substring : ")
if fWord in l2:
    newParaGraph = l2.replace(fWord, fRep)
    print(f"The \"{fWord}\" got replace by \"{fRep}\" : ")
    print(newParaGraph)
    print()
else:
    print("enter a valid substring which is present in the paragraph.")

sum = 0
def toSumDigits(number):
    global sum
    if(number>0):
        toSum = number%10
        sum = sum+toSum
        toSumDigits(int(number/10))
number = int(input("Enter a number : "))
if number>10:
    toSumDigits(number)
    print(f"The sum of digits of number : {sum}")
else:
    print(f"The sum of digits of number : {number}")

import datetime
name = (('Bunny',17),('Bhanu',57),('Hrithik',7))
tupmark = ()
tupdate = ()
ch=1
while ch!= 0 :
    print('1:add student marks \n2:Display students with specified key. \n3:Enter students’ admission date ')
    op=int(input('enter your option: '))
    while op>0 and op<=4:
        if op==1:
            i = int(input('Enter roll no of student : '))
            j = 0
            flag = False
            l1 = list(name)
            for k in name :
                if k[1] == i :
                    flag = True
                    break
                j = j+1
            if flag == False :
                print('enter the valid number')
                break
            print('enter the the marks of student : ')
            Maths = int(input('Enter the Maths marks '))
            AT = int(input('Enter the AT marks '))
            Python = int(input('Enter the Python marks '))
            tup1 = 0
            tup1 = ( name[j] + ( Maths , AT , Python))
            tupmark = tupmark + tup1
            sum1 = Maths + AT + Python
            avg =sum1/3
            print(tup1 , '\navg = ',avg ," \nsum = ",sum1)
            break
        elif op==2:
            for k in name :
                print(k)
            break
        elif op==3:
            for k in name :
                print('Enter the admission date of ',k[0])
                dd = int(input('admission date '))
                mm = int(input('admission month '))
                yyyy = int(input('admission year '))
                date1 = datetime.date(yyyy,mm,dd)
                tup2 = (k[0],k[1],date1)
                tupdate = tupdate + tup2
                print(dd,'/',mm,'/',yyyy)
            print(tupdate)
            break
    print('would you like to continue:[0/1]')
    ch=int(input('enter your choice: '))

s1 = input('Enter string 1: ')
s2 = input('Enter string 2: ')
a = set(s1)
b = set(s2)
choice = -1
while(choice != 0):
    print('\nSelect your choice\n')
    print('1. Display common letters in string 1 and 2')
    print('2. Display letters which are in string 1 but not in string 2')
    print('3. Display set of all letters from both the strings')
    print('4. Display set of letters which are in present in string 1 but not in string 2')
    print('Press 0 to Exit the Program')
    choice=int(input('Enter your choice: '))
    if(choice==1):
        c=a.intersection(b)
        print('\nCommon Letters in the input strings are:')
        print(c)
    elif(choice==2):
        c=a.difference(b)
        print('\nLetters which are in the first string but not in the second string are:')
        print(c)
    elif(choice==3):
        c=a.union(b)
        print('\nSet of all letters from both the strings are:')
        print(c)
    elif(choice==4):
        c=a.symmetric_difference(b)
        print('\nSet of letters which are in two strings but not common are:')
    else:
        print('\nInvalid input!')
        break

choice = -1
while(choice != 0):
    print("\n")
    print('Enter your Choice:')
    print('a) Create key/value pair dictionary.')
    print('b) Update/concatenate and delete item from an existing dictionary.')
    print('c) Find a key and print its value from the key-value pair.')
    print('Press 0 to exit')
    choice=int(input('Enter your choice: '))
    if(choice==1):
        a={2}
        n=int(input('Enter how many key/value pairs you want to enter: '))
        for x in range(n):
            k=input('Enter the key: ')
            v=input('Enter the value: ')
            a.update({k:v})
        print("The entered dictionary is: ")
        print(a)
    elif(choice==2):
        while(True):
            print('Enter your choice \n1.Update\n2.Concatenate\n3.Delete\nPress 0 to go back to the Main Menu')
            q=int(input())
            if(q==1):
                c=input('Enter the key to be updated:')
                d=input('Enter the updated value:')
                a[c]=d
                print('Updated Dictionary:')
                print(a)
            elif(q==2):
                c=input('Enter the key to be added:')
                d=input('Enter the key value:')
                a[c]=d
                print('Updated Dictionary:')
                print(a)
            elif(q==3):
                c=input('Enter the key to be deleted:')
                del a[c]
                print('Updated Dictionary:')
                print(a)
            elif(q==0):
                break
        else:
            print('Invalid Choice')
    elif(choice==3):
        b=input('Enter the key to find its corresponding value:')
        print(a.get(b))
    else:
        print('EXIT!!!')