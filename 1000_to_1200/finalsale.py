# Question Link: https://www.codechef.com/problems/FINALSALE

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_total = 0
    
    for i in range(n):
        sums = sum(arr[:i])
        total = sums + (2 * arr[i])
        max_total = max(max_total, total)
    
    print(max_total)