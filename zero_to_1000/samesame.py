# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    b = input()
    substrings = []
    for i in range(n - m + 1):
        substrings.append(a[i:i+m])
    # print(substrings)
    res = []
    for sub in substrings:
        temp = 0
        for i in range(m):
            if sub[i] != b[i]:
                temp += 1
        res.append(temp)
    print(min(res))