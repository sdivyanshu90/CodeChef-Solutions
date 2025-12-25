# Question Link: https://www.codechef.com/problems/SINGLEUSE

# cook your dish here
from math import ceil

for _ in range(int(input())):
    x, y, h = map(int, input().split())
    rem = x - h
    res = 1
    if rem > 0:
        res += ceil(rem / y)
    print(res)