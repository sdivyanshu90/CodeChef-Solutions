# Question Link: https://www.codechef.com/problems/BIN_BAT

# cook your dish here
import math

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    matches = int(math.log2(n))
    print((a + b) * (matches - 1) + a)