# Question Link: https://www.codechef.com/problems/RECTSQ

# cook your dish here
import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(math.lcm(n,m) // math.gcd(n,m))