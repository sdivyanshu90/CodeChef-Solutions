# Question Link: https://www.codechef.com/problems/CARRYGOLD

# cook your dish here
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    req = (n + 1) * y
    if req >= x:
        print("YES")
    else:
        print("NO")