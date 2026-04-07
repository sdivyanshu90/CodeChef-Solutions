# Question Link: https://www.codechef.com/problems/DIVEMAKEEQ

# cook your dish here
from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    divisor = gcd(*a)
    count = 0
    for num in a:
        if num > divisor:
            count += 1
    print(count)