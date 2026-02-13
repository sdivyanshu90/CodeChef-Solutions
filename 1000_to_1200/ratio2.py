# Question Link: https://www.codechef.com/problems/RATIO2

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x >= 2*y or y >= 2*x:
        print(0)
    else:
        mini = min(x, y)
        maxi = max(x, y)
        print(abs((maxi // 2) - mini))