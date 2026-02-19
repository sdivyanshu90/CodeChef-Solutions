# Question Link: https://www.codechef.com/problems/MASKPOL

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(min(m, n - m))