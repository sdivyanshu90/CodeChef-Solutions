# cook your dish here
n = int(input())
c = list(map(int, input().split()))
sumc = sum(c)
total = (n * (n + 1)) // 2
if sumc == total:
    print("YES")
else:
    print("NO")