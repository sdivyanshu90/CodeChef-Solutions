# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    count = {}
    for k, v in zip(a, b):
        if k in count:
            count[k] = max(count[k], v)
        else:
            count[k] = v
            
    res = 0
    for nutr, val in count.items():
        if val > 0:
            res += val
            
    print(res)