# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    if n >= k * (k + 1) // 2:
        print("YES")
    else:
        print("NO")