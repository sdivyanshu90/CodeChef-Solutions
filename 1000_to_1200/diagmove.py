# Question Link: https://www.codechef.com/problems/DIAGMOVE

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    diff = abs(x - y)
    if diff % 2 == 0:
        print("YES")
    else:
        print("NO")