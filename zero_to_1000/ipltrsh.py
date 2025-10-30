# Question Link: https://www.codechef.com/problems/IPLTRSH

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    if n < m:
        print(0)
    else:
        print(n - m)