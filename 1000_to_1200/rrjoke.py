# cook your dish here
for _ in range(int(input())):
    n = int(input())
    
    for _ in range(n):
        input()

    res = 0
    for i in range(1, n + 1):
        res ^= i
    print(res)