# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    if n // 2 >= m:
        print("Yes")
    else:
        print("No")