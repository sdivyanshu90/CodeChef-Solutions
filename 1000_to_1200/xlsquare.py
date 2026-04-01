# Question Link: https://www.codechef.com/problems/XLSQUARE

# cook your dish here
from math import isqrt

for _ in range(int(input())):
    n, a = map(int, input().split())
    print(a * isqrt(n))