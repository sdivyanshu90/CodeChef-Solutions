# cook your dish here
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    nth = n - (k + m - 1) // m
    mth = m - (k + n - 1) // n
    print(max(n * mth, m * nth))