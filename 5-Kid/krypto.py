"""
INPUT
E / D (Encryption or Decryption)
a
b
A
B
Message
OUTPUT
Crypto Message or Plain Text
"""

opt = input()
a = int(input())
b = int(input())
A = int(input())
B = int(input())
x = int(input())

M = a*b - 1
e = A*M + a
d = B*M + b
n = (e*d - 1)/M

if opt == 'E':
    y = (x * e) % n
    print(int(y))

elif opt == 'D':
    y = (x *d ) % n
    print(int(y))
