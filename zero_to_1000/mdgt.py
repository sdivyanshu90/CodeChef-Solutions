# cook your dish here
for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    bhoomi = h[-1]
    pos = n - 1
    res = 0
    
    while any(x >= bhoomi for x in h[:pos]):
        pos -= 1
        res += 1
    print(res)