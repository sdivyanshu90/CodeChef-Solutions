# Question Link: https://www.codechef.com/problems/PRODUCT

# cook your dish here
import math

for _ in range(int(input())):
    b, c = map(int, input().split())
    print(c // math.gcd(b, c))