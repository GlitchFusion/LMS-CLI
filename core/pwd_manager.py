shift = 3

# password hasing - encoding
def encode_password(pwd):
    encoded_pwd = ""
    for char in pwd:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encoded_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encoded_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encoded_pwd += encoded_char
    return encoded_pwd

# password hashing - decoding
def decode_password(pwd):
    decoded_pwd = ""
    for char in pwd:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decoded_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                decoded_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            decoded_pwd += decoded_char
    return decoded_pwd