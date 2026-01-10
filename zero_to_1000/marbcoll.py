# Question Link: https://www.codechef.com/problems/MARBCOLL

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    set_a = set(a)
    not_collected = list(range(1, m + 1))
    res = len(not_collected)
    for item in set_a:
        if item in not_collected:
            res -= 1
    print(res)