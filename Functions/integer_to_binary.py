
"""Function that takes an integer as an input and outputs its 8 bit value"""


def int_to_bytes(x):
    bytes = bin(x)[2:].zfill(8)
    print(bytes)
int_to_bytes()
