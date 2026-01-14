# cook your dish here
for _ in range(int(input())):
    a = list(map(str, input().split()))
    x, y = map(str, input().split())
    print(a[min([a.index(x), a.index(y)])])