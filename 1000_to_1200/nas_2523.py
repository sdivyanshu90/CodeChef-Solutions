# Question Link: https://www.codechef.com/problems/NAS_2523

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        res = []
        for i in range(1, n + 1):
            res.append(i)
        print(*res[::-1])
    else:
        print(-1)