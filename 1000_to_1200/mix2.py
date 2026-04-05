# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            res += (arr[i] * arr[j])
            # print(f"arr[i]: {arr[i]}, arr[j]: {arr[j]}")
            
    print(res)