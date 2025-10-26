# Question Link: https://www.codechef.com/problems/CALINTAKE

# cook your dish here
x, y, z = map(int, input().split())
res = x - (y * z)
if res > 0:
    print(res)
else:
    print(-1)