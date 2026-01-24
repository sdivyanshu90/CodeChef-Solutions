# Question Link: https://www.codechef.com/problems/DISCOOKIE

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())

    if m < n:
        print(n - m)
    else:
        lower = (m // n) * n
        upper = lower + n
        print(min(m - lower, upper - m))