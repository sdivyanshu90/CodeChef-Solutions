# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    unrated = 2*n - x
    if unrated >= x:
        print(0)
    else:
        print(2*x - 2*n)