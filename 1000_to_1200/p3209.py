# cook your dish here
from math import gcd

for _ in range(int(input())):
    n = int(input())
    gcds = []
    for i in range(1, n + 1):
        gcds.append([i, gcd(i, n)])
        
        
    # print("Non-sorted: ", gcds)
    
    gcds.sort(key = lambda x: (-x[1]))
    
    # print("Sorted: ", gcds)
    res = []
    for i, j in gcds:
        res.append(i)
        
    print(*res)