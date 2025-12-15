# Question Link: https://www.codechef.com/problems/SPCP2

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    req = 0
    if x % 100 == 0:
        req = x // 100
    else:
        req = x // 100 + 1
    if n > req:
        print(0)
    else:
        print(req - n)