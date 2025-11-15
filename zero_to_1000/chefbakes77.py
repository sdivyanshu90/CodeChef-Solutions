# Question Link: https://www.codechef.com/problems/CHEFBAKES77

# cook your dish here
import math

n, x, y = map(int, input().split())
cap = y // x
print(math.ceil(n / cap))