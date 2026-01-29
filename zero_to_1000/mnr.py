# Question Link: https://www.codechef.com/problems/MNR

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = float("inf")
    for s in [n, n - 1, n - 2]:
        for i in range(n - s + 1):
            ans = min(ans, a[i + s - 1] - a[i])
    print(ans)