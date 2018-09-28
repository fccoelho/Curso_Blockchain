"""
Implementation of MD5 by Rafael Barsotti
"""
import math as m


def getABCD():
    a = int("0x67452301", 16)
    b = int("0xefcdab89", 16)
    c = int("0x98badcfe", 16)
    d = int("0x10325476", 16)


def getKTable():
    l = []
    for i in range(65):
        k_i = floor(2 ** 32 * abs(m.sin(i + 1)))
        l.append(k_i)
    return l


def getS():
    s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
         5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
         4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
         6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
    return s


def asciiMessage(message):
    ascii = ''
    for i in message:
        ascii += str(ord(i))
    return ascii


def wrap64(number):
    return number % 2 ** 64


def binString(message):
    message = bin(int(message))
    message = message[2:]
    return message


def paddingMessage(message):
    m = len(message) % 512
    m_1 = (512 - 64 - m)
    append_1 = '1' + '0' * (m_1 - 1)
    append_2 = bin((len(message) % 2 ** 64))
    append_2 = append_2[2:]
    if len(append_2) < 64:
        zeros = '0' * (64 - len(append_2))
        append_2 += zeros
    message += append_1 + append_2
    return message


def hashMD5(message):
    original = message
    hash_message = paddingMessage(message)
    print(original, hash_message)


if __name__ == "__main__":
    from hashlib import md5
    hashMD5(b"Hello World")
    h = md5(b'Hello World')
    print("Correct Hash: ", h.hexdigest())
