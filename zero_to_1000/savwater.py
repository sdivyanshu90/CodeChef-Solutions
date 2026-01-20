# Question Link: https://www.codechef.com/problems/SAVWATER

# cook your dish here
for _ in range(int(input())):
    h, x, y, c = map(int, input().split())
    grey =  x + y // 2
    water = h * grey
    if c >= water:
        print("YES")
    else:
        print("NO")