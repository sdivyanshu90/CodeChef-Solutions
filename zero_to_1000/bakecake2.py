# Question Link: https://www.codechef.com/problems/BAKECAKE2

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    for i in range(len(a)):
        if a[i] >= b[i]:
            res += (a[i] - b[i])
    print(res)