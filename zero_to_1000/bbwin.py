# Question Link: https://www.codechef.com/problems/BBWIN

# cook your dish here
import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    diff = a - b

    if diff >= 10:
        print(0)
    else:
        print(math.ceil((10 - diff) / 3))