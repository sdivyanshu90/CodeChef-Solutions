# Question Link: https://www.codechef.com/problems/PRICECON

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    initial = sum(p)
    for i in range(n):
        if p[i] > k:
            p[i] = k
    final = sum(p)
    print(initial - final)