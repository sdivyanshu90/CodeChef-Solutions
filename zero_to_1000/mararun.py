# cook your dish here
for _ in range(int(input())):
    n, d, a, b, c = map(int, input().split())
    dist_covered = n * d
    if dist_covered < 10:
        print(0)
    elif 10 <= dist_covered < 21:
        print(a)
    elif 21 <= dist_covered < 42:
        print(b)
    else:
        print(c)