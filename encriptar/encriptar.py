import binascii


def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)


with open("rsa_values.txt", "r") as values_file:
    for line in values_file:
        element = line.split(" ")
        if element[0] == 'n':
            n = int(element[2])
        elif element[0] == 'e':
            e = int(element[2])
        elif element[0] == 'd':
            d = int(element[2])
        elif element[0] == 'p':
            p = int(element[2])
        elif element[0] == 'q':
            q = int(element[2])

message = b"RSA isn't really that hard"

print("n:"+str(n))
print("e:"+str(e))

m = string2int(message)

ciphertext = pow(m, e, n)
print("Cipher text: " + str(ciphertext))
