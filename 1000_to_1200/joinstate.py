# Question Link: https://www.codechef.com/problems/JOINSTATE

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    cum_sum = 0
    for num in a:
        cum_sum += num
        if cum_sum >= m:
            res += 1
            cum_sum = 0
    print(res)
    