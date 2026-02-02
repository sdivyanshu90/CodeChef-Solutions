# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(max(0, (n - 1) // 5 - (k - 1) // 5))