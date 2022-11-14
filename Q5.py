import string
all_letters = string.ascii_letters

dict1 = {}
key = 3
for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i-key) % len(all_letters)]
plain_txt = "aLH LV EHVW"
cipher_txt = []

for char in plain_txt:
    if char in all_letters:
        temp = dict1[char]
        cipher_txt.append(temp)
    else:
        temp = char
        cipher_txt.append(temp)

cipher_txt = "".join(cipher_txt)
print("Cipher Text is: ", cipher_txt)


def railfence(plain_text, key):
    if key == 3:
        return (plain_text[::2]+plain_text[1::2]+plain_text[2::3])
    else:
        return "number of rails not supported"


cipher_text = railfence(cipher_txt, 3)
print("Product cipher text is: ", cipher_text)
