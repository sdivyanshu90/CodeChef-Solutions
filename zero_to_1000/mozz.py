# Question Link: https://www.codechef.com/problems/MOZZ

# cook your dish here
from math import ceil

for _ in range(int(input())):
    x, y, r = map(int, input().split())
    sticks = x + r // 30
    print(ceil(sticks / y))