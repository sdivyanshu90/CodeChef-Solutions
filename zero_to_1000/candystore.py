# Question Link: https://www.codechef.com/problems/CANDYSTORE

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > y:
        print(y)
    elif x < y:
        print((y - x) * 2 + (x))
    else:
        print(x)