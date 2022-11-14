# For Decryption - Brute force attack

import string
all_letters = string.ascii_letters

dict1 = {}
for key in range(1, 27):
    z = key
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i+z) % len(all_letters)]
    plain_txt = "aLH LV EHVW"
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
