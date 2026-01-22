# Question Link: https://www.codechef.com/problems/MARBLES

# cook your dish here
from math import comb

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(comb(n - 1, k - 1))