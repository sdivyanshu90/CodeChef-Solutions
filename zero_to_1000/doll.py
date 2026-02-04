# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    res = 0
    for height in h:
        if height > k:
            res += 1
    print(res)