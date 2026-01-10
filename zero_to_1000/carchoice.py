# Question Link: https://www.codechef.com/problems/CARCHOICE

# cook your dish here
for _ in range(int(input())):
    x1, x2, y1, y2 = map(int, input().split())
    car1 = y1 / x1
    car2 = y2 / x2
    if car1 > car2:
        print(1)
    elif car2 > car1:
        print(-1)
    else:
        print(0)