# Question Link: https://www.codechef.com/problems/CHANGEPOS

# cook your dish here
for _ in range(int(input())):
    sx, sy, ex, ey = map(int, input().split())
    if sx != ex and sy != ey:
        print(1)
    else:
        print(2)