# Question Link: https://www.codechef.com/problems/FIZZBUZZ2303

# cook your dish here
import math

for _ in range(int(input())):
    n = int(input())
    print(math.factorial(n) // math.factorial(n - 2))