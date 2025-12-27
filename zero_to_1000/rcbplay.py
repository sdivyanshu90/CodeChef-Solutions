# Question Link: https://www.codechef.com/problems/RCBPLAY

# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    score = x + (z * 2)
    if score >= y:
        print("YES")
    else:
        print("NO")