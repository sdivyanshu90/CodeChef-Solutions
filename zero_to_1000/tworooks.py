# Question Link: https://www.codechef.com/problems/TWOROOKS

# cook your dish here
for _ in range(int(input())):
    x1, x2, y1, y2 = map(int, input().split())
    if x1 == y1 or x2 == y2:
        print("YES")
    else:
        print("NO")