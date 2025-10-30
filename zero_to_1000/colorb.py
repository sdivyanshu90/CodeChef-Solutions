# Question Link: https://www.codechef.com/problems/COLORB

# cook your dish here
r, b = map(int, input().split())
g = 0
if r > b:
    g = b
    r = (r - g)
    b = 0
elif r < b:
    g = r
    b = (b - g)
    r = 0
else:
    g = r
    r = 0
    b = 0
    
print(5 * g + 2 * b + r)
