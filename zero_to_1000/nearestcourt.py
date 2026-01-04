# Question Link: https://www.codechef.com/problems/NEARESTCOURT

# cook your dish here
from math import ceil

for _ in range(int(input())):
    x, y = map(int, input().split())
    diff = abs(x - y)
    print(ceil(diff / 2))