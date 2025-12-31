# cook your dish here
for _ in range(int(input())):
    length, width, target = map(int, input().split())
    res = float('inf')
    for l in range(1, length + 1):
        for w in range(1, width + 1):
            peri = 2 * (l + w)
            diff = abs(peri - target)
            if diff < res:
                res = diff
    print(res)