punct = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("Enter a string: ")
no_punct = ""
for char in my_str:
    if char not in punct:
        no_punct = no_punct + char
print("String with punctuation:",my_str)
print("String without punctuation:",no_punct)
print("Words in Alphabetical order:")
words = no_punct.split()
words.sort()
for word in words:
    print(word)