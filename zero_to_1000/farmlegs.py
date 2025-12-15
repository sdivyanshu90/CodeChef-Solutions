# Question Link: https://www.codechef.com/problems/FARMLEGS

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    res = 0
    while n > 0:
        if n >= 4:
            n -= 4
        else:
            n -= 2
        res += 1
        
    print(res)