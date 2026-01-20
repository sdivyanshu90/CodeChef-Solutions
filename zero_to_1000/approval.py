# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    
    res = 0
    while True:
        avg = sum(a) / len(a)
        if avg >= 7:
            print(res)
            break

        a[a.index(min(a))] = 10
        res += 100