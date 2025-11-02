# Question Link: https://www.codechef.com/problems/BULLBEAR

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    diff = x - y
    if diff > 0:
        print("LOSS")
    elif diff == 0:
        print("NEUTRAL")
    else:
        print("PROFIT")