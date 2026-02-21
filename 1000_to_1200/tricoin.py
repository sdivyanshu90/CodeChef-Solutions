# cook your dish here
import math

for _ in range(int(input())):
    n = int(input())
    print(int((math.isqrt(1 + 8*n) - 1) // 2))