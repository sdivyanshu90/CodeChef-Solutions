# cook your dish here
for _ in range(int(input())):
    n, k, x, y = map(int, input().split())
    red_k = k * x
    rem = n - k
    res = min(rem * x, rem * y)
    print(res + red_k)