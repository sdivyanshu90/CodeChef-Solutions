# cook your dish here
import math

for _ in range(int(input())):
    x, y = map(int, input().split())

    if y <= x:
        print(0)
    else:
        t = math.ceil(10 * (y - x) / (100 - y))
        print(t)