# Question Link: https://www.codechef.com/problems/CHEFARRP

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    
    for i in range(n):
        s = 0
        p = 1
        for j in range(i, n):
            s += a[j]
            p *= a[j]
            
            if p == s:
                count += 1
            
            if p > 10**15:
                break
                
    print(count)