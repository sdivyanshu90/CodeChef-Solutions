# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            res += 1
    print(res)