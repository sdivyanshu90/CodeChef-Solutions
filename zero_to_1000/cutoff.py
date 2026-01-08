# Question Link: https://www.codechef.com/problems/CUTOFF

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # your code goes here
    a.sort(reverse = True)
    if x == n:
        print(min(a) - 1)
    else:
        print(a[x - 1] - 1)