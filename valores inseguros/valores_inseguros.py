import binascii


def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

def find_inverse_power(x, n):
    high = 1
    while pow(high, n) <= x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1


with open("values.txt", "r") as values_file:
    for line in values_file:
        element = line.split(" ")
        if element[0] == 'n':
            n = int(element[2])
        elif element[0] == 'e':
            e = int(element[2])
        elif element[0] == 'ciphertext':
            ciphertext = int(element[2])


# If M^e < n, the modulus doesn't affects to the equation.
# So c = m^e
# If e = 3, sqrt3(c) = sqrt3(m^3) --> sqrt3(c) = m
# And sqrt3(c) = c ^ (1/3)
# So c ^ (1/3) = m
decrypted = find_inverse_power(ciphertext, 3)
m = int2string(decrypted)
print("ZD{" + m + "}")

