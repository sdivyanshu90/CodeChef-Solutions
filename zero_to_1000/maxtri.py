# Question Link: https://www.codechef.com/problems/MAXTRI

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a, b = n - 1, n - 2
    if 2 * max(a, b, n) < a + b + n:
        print(a+b+n)
    else:
        print(-1)