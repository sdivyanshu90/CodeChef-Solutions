# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    if x == 0:
        print(n)
    elif x == n:
        print(2*x - 1)
    else:
        print(2*x + (n - x))