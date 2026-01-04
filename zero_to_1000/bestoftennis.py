# Question Link: https://www.codechef.com/problems/BESTOFTENNIS

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > y:
        print(x + (x - 1))
    else:
        print(y + (y - 1))