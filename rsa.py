import math
from sympy import isprime
import base64

def main():
    # Getting the first prime number
    p = int(input("First prime number: "))

    while not isprime(p):
        print(f"{p} is not prime, try again")
        p = int(input("First prime number: "))

    # Getting the second prime number
    q = int(input("Second prime number: "))

    while not isprime(q) or q == p:
        if not isprime(q):
            print(f"{q} is not prime, try again")
        else:
            print("q cannot be the same value as p, try again")    
        q = int(input("Second prime number: "))

    # Obtaining value n and phi_n
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Getting the public key value, e
    e = int(input("Public exponent: "))

    while 1 >= e or e >= phi_n or not math.gcd(e, phi_n) == 1:
        if 1 >= e or e >= phi_n:
            print(f"{e} is not in the range of (1, {phi_n}), try again")
        else:
            print(f"gcd between {phi_n} and {e} is not 1, try again")
            print("hint: common values of e include 3, 13, 17, 65537")
        e = int(input("Public exponent: "))

    # Solving the private key value, d
    d = pow(e, -1, phi_n)

    print(f"Private Key: ({d}, {n})")
    
    # Obtaining the mesaage
    message = input("Message to encrypt: ")

    # Display public key
    print(f"Public Key: ({e}, {n})")

    # Encrypting the message
    char_arr = [] # Array of all characters
    encrypt_arr = [] # Array of all ciphertexts for corresponding characters

    # Filling up array of characters
    for element in message:
        char_arr.append(element)

    # Encrypting all characters in char_arr, storing in encrypt_arr
    for x in char_arr:
        encrypt_arr.append(pow(ord(x), e, n))

    # Converting all integers in encrypt_arr to binary data
    encrypt_bytes = []
    for a in encrypt_arr:
        byte_length = (a.bit_length() + 7) // 8
        byte_rep = a.to_bytes(byte_length, 'big')
        encrypt_bytes.append(byte_rep)

    # Using PEM formatting to change all data into text-based formatting
    string_arr = [] # Storing text in this array
    for byte in encrypt_bytes:
        string_arr.append(base64.b64encode(byte).decode('utf-8'))

    # Concatenating array into one large string
    concat_str = ""
    for str in string_arr:
        concat_str += str

    # Printing the encrypted message
    print("-----BEGIN CIPHERTEXT-----")
    print(concat_str)
    print("-----END CIPHERTEXT-----")

if __name__ == '__main__':
    main()