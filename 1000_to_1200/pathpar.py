# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    if n % 2 == 0 or k == 1:
        print("YES")
    else:
        print("NO")