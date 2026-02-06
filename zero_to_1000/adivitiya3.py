# Question Link: https://www.codechef.com/problems/ADIVITIYA3

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = []
    for num in a:
        if num >= k:
            res.append(num % k)
    if not res:
        print(-1)
    else:
        print(min(res))