# Question Link: https://www.codechef.com/problems/PARLIAMENT

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    half = x // 2
    rem = x - half
    if y >= rem:
        print("YES")
    else:
        print("NO")