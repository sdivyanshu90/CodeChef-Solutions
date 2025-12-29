# Question Link: https://www.codechef.com/problems/DPOLY

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if a[i] != 0:
            res = i
            
    print(res)