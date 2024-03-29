# * For Encryption - using ceaser cipher

import string
all_letters = string.ascii_letters  # A list containing all characters

dict1 = {}
key = 3
for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i+key) % len(all_letters)]
plain_txt = "Hello Bunny"
cipher_txt = []

# loop to generate ciphertext
for char in plain_txt:
    if char in all_letters:
        temp = dict1[char]
        cipher_txt.append(temp)
    else:
        temp = char
        cipher_txt.append(temp)

cipher_txt = "".join(cipher_txt)
print("Cipher Text is: ", cipher_txt)
