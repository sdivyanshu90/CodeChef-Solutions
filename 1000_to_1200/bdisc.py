# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = []
    res.append(arr[0])
    for i in range(1, n):
        if arr[i] - i >= 0:
            res.append(arr[i] - i)
        
    print(sum(res))