# Question Link: https://www.codechef.com/problems/PROC18A

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    res = []
    for i in range(n - k + 1):
        window = a[i : i + k]
        res.append(sum(window))
        
    print(max(res))