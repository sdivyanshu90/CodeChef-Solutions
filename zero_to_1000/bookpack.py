# Question Link: https://www.codechef.com/problems/BOOKPACK

# cook your dish here
from math import ceil

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if y > z:
        need = ceil(y / z)
        print(x * need)
    else:
        print(x)