# Question Link: https://www.codechef.com/problems/MIXINGLIQ

# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    res = 0
    
    while a > 0 and b > 1:
        a -= 1
        b -= 2
        res += 3
        
    print(res)