# cook your dish here
from math import ceil

for _ in range(int(input())):
    a, b = map(int, input().split())
    res = 0
    if a == b:
        print(0)
    else:
        
        while a != b:
            if a > b:
                temp = ceil(a / 2)
                res += temp
                a -= temp
            else:
                temp = ceil(b / 2)
                res += temp
                b -= temp
                
        print(res)