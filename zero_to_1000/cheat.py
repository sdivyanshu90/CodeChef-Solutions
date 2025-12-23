# cook your dish here
for _ in range(int(input())):
    n = int(input())
    temp = []
    for i in range(2, n + 1, 7):
        temp.append(i)
    res = 0
    for num in temp:
        if num <= n:
            res += 1
    print(res)