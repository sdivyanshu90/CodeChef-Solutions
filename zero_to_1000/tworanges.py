# Question Link: https://www.codechef.com/problems/TWORANGES

# cook your dish here
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    mini = min(a, b, c, d)
    maxi = max(a, b, c, d)
    res = 0
    for i in range(mini, maxi + 1):
        if a <= i <= b or c <= i <= d:
            res += 1
    print(res)