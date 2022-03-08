# l1 = [1,2,3,4,5,6,7,8,9]
# summ = 0
# print("Current array is:",l1)

# for i in l1:
#     if (i%2==0):
#         summ = i + i
# print("Sum of all even elements are:",summ)

# count = 0
# for j in l1:
#     if (j%3==0):
#         count = count + 1
# print("The number of elements which are divisible by 3 are:",count)
# print("\n")

# l1.append(10)
# l1.append(11)
# print("Array after adding two elements at the end:",l1)
# print("\n")

# for i in l1:
#     if (i%2==1):
#         l1.remove(i)
# print("Array after deleting all the odd elements :",l1)

l2 = []
l2 = input("Enter multiple words or a paragraph: ")

print("No.of character in a list are :",len(l2))

l2words = l2.split(" ") 
print("No.of words in a list are :",len(l2words))

