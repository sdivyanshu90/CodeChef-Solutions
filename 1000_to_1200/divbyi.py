# Question Link: https://www.codechef.com/problems/DIVBYI

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    i, j = 0, n - 1
    res = []
    
    while i < j:
        res.append(j + 1)
        res.append(i + 1)
        i += 1
        j -= 1
    
    if i == j:
        res.append(i + 1)
    
    print(*res[::-1])