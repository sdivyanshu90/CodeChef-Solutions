# Question Link: https://www.codechef.com/problems/BRUNCH

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    can = x // y
    if can > 20:
        print(20)
    else:
        print(can)