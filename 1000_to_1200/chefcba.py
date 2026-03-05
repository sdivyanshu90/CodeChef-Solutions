# cook your dish here
a = list(map(int, input().split()))
a.sort()

if a[0] * a[3] == a[1] * a[2]:
    print("Possible")
else:
    print("Impossible")