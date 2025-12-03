# Question Link: https://www.codechef.com/problems/EXPERT

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    perc = (y / x) * 100
    if perc >= 50:
        print("YES")
    else:
        print("NO")