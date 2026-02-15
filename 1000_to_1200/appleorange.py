# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    while m != 0:
        n, m = m, n % m
    print(n)