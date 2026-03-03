# Question Link: https://www.codechef.com/problems/ICL1902

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    res = 0
    
    while n != 0:
        s = int((n) ** 0.5)
        n -= (s * s)
        res += 1
    
    print(res)