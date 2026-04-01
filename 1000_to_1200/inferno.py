# Question Link: https://www.codechef.com/problems/INFERNO

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    h = list(map(int, input().split()))

    m1 = max(h)
    m2 = sum((i + x - 1) // x for i in h)
    print(min(m1, m2))