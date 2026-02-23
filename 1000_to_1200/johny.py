# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    fav = a[k - 1]
    a.sort()
    print(a.index(fav) + 1)