# Question Link: https://www.codechef.com/problems/SELFDEF

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for num in a:
        if 10 <= num <= 60:
            res += 1
    print(res)