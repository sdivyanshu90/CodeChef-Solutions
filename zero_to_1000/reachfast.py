# Question Link: https://www.codechef.com/problems/REACHFAST

# cook your dish here
from math import ceil

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    res = ceil((abs(a - b) / c))
    print(res)