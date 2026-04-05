# Question Link: https://www.codechef.com/problems/BIT2A

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = [0] * n
    
    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                count += 1
                
        res[i] = count
        
    print(*res)