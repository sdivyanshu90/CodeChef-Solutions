# Question Link: https://www.codechef.com/problems/BFLY

# cook your dish here
for _ in range(int(input())):
    r, g, b = map(int, input().split())
    if r > (g + b) or g > (r + b) or b > (g + r):
        print("NO")
    else:
        print("YES")