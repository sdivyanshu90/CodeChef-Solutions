# Question Link: https://www.codechef.com/problems/ANUUND

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    
    if n > 2:
        for i in range(1, n - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    print(*arr)