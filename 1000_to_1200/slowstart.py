# cook your dish here
import math

for _ in range(int(input())):
    x, h = map(int, input().split())
    half = x // 2
    if half > h:
        print(1)
    elif 5 * half > h:
        print(math.ceil(h / half))
    else:
        rem = h - (5 * half)
        print(5 + math.ceil(rem / x))