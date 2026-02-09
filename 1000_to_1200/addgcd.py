# cook your dish here
from math import gcd

for _ in range(int(input())):
    x,y = map(int, input().split())
    if gcd(x, y) > 1:
        print(0)
    else:
        if gcd(x + 1, y) > 1 or gcd(y + 1, x) > 1:
            print(1)
        else:
            print(2)