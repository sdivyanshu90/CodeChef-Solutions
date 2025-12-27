# cook your dish here
import copy

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = copy.deepcopy(a)
    sorted_a = sorted(b)
    
    res = sorted_a[0] + sorted_a[1]
    for i in range(n - 1):
        val = a[i] + (a[i + 1] // 2)
        res = min(res, val)
    print(res)