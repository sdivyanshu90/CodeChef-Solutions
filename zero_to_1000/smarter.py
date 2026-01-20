# cook your dish here
from math import ceil

for _ in range(int(input())):
    l, v1, v2 = map(int, input().split())
    t1 = ceil(l / v1)
    t2 = ceil(l / v2)
    diff = t1 - t2
    if t1 == t2:
        print(-1)
    elif diff >= 2:
        print(diff - 1)
    else:
        print(0)