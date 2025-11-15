# Question Link: https://www.codechef.com/problems/CABS

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > y:
        print("SECOND")
    elif y > x:
        print("FIRST")
    else:
        print("ANY")