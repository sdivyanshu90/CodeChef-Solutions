# Question Link: https://www.codechef.com/problems/PASSINGGR

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    chef = a[0]
    res = 1
    for i in range(1, len(a)):
        if a[i] >= chef:
            res += 1
            
    print(res)