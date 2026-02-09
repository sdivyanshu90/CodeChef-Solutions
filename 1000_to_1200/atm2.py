# Question Link: https://www.codechef.com/problems/ATM2

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = ""
    for p in a:
        if p > k:
            res += "0"
            continue
        else:
            k -= p
            res += "1"
    print(res)