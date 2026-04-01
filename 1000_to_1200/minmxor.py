# Question Link: https://www.codechef.com/problems/MINMXOR

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(*range(n, 0, -1))
    else:
        print(-1)