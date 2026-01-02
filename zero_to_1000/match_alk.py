# cook your dish here
for _ in range(int(input())):
    res = []
    for _ in range(22):
        a, b = map(int, input().split())
        # print(f"a: {a}, b: {b}")
        temp = a + b * 20
        res.append(temp)
    print(res.index(max(res)) + 1)