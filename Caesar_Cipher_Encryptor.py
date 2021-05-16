def caesarCipherEncryptor(string, key):
    cipher = []
    for letter in string:
        if 96 < ord(letter) + key < 123:
            cipher.append(chr(ord(letter) + key))
        elif key < 26:
            cipher.append(chr(ord(letter) + key - 26))
        else:
            cipher.append(chr(ord(letter) + key % 26))
    cipher = ''.join(cipher)
    return cipher
