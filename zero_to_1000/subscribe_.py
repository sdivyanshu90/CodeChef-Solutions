# Question Link: https://www.codechef.com/problems/SUBSCRIBE_

# cook your dish here
for _ in range(int(input())):
    x, n = map(int, input().split())
    if x % 6 != 0:
        print(((x // 6) * n) + n)
    else:
        print((x // 6) * n)