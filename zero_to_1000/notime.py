# cook your dish here
n, h, x = map(int, input().split())
t = list(map(int, input().split()))
flag = False
for time in t:
    if time + x >= h:
        flag = True

if flag:
    print("YES")
else:
    print("NO")