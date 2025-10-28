# Question Link: https://www.codechef.com/problems/WEIGHTLIFT   

# cook your dish here
a, b, c, d, e, f = map(int, input().split())
res = 0
if a > b:
    res += a
else:
    res += b
    
if c > d:
    res += c
else:
    res += d
    
if e > f:
    res += e
else:
    res += f
    
print(res)