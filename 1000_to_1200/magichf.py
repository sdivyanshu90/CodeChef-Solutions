# Question: https://www.codechef.com/START11B/problems/MAGICHF

# cook your dish here
for _ in range(int(input())):
    n, x, s = map(int, input().split())
    res = x
    for _ in range(s):
        a, b = map(int, input().split())
        if res == a:
            res = b
        elif res == b:
            res = a
    print(res)