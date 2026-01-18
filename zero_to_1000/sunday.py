# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sat, sun = [6, 13, 20, 27], [7, 14, 21, 28]
    res = 8
    for day in a:
        if day in sat or day in sun:
            continue
        else:
            res += 1
    print(res)