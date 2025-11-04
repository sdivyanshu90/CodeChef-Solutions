# Question Link: https://www.codechef.com/problems/CHAIRS_

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if (x - y) > 0:
        print(x - y)
    else:
        print(0)