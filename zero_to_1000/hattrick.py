# cook your dish here
for _ in range(int(input())):
    a = list(map(str, input().split()))
    if "WWW" in "".join(a):
        print("YES")
    else:
        print("NO")