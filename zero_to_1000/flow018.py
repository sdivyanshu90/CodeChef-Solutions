# Question Link: https://www.codechef.com/problems/FLOW018

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    res = 1
    for i in range(2, n + 1):
        res *= i
    print(res)