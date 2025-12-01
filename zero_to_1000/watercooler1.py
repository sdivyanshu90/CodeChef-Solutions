# Question Link: https://www.codechef.com/problems/WATERCOOLER1

# cook your dish here
for _ in range(int(input())):
    x, y, m = map(int, input().split())
    rent = x * m
    if rent < y:
        print("YES")
    else:
        print("NO")