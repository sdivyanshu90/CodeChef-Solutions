# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    if m >= n:
        print(-1)
    else:
        print(2*m + 1)