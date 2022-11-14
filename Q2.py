# Railfence cipher

cipher_text = ""


def railfence(plain_text, key):
    if key == 3:
        return (plain_text[::2]+plain_text[1::2]+plain_text[2::3])
    else:
        return "number of rails not supported"


cipher_text = railfence("xie is best ", 3)
print(cipher_text)
